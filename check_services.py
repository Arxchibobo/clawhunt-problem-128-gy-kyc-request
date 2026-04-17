#!/usr/bin/env python3
"""
Service Availability Checker for Overseas Access Tools

Checks if key virtual phone number and virtual card services are accessible.
Useful for verifying which services are available from your location.

Usage:
    python check_services.py

Requirements:
    - Python 3.6+
    - No external dependencies (uses stdlib only)
"""

import urllib.request
import urllib.error
import socket
import ssl
from typing import Dict, List, Tuple
import json


# Service definitions
SERVICES = {
    "Virtual Phone Numbers": [
        ("TextNow", "https://www.textnow.com"),
        ("Hushed", "https://www.hushed.com"),
        ("MySudo", "https://mysudo.com"),
        ("Google Voice", "https://voice.google.com"),
        ("Twilio", "https://www.twilio.com"),
        ("5sim", "https://5sim.net"),
        ("SMS-Activate", "https://sms-activate.org"),
    ],
    "Virtual Credit Cards": [
        ("Depay", "https://depay.one"),
        ("WildCard", "https://wildcard.com.cn"),
        ("Revolut", "https://www.revolut.com"),
        ("Wise", "https://wise.com"),
    ],
    "AI Services": [
        ("Claude", "https://claude.ai"),
        ("OpenAI", "https://openai.com"),
        ("GitHub", "https://github.com"),
        ("Anthropic", "https://www.anthropic.com"),
    ],
}


def check_url(url: str, timeout: int = 10) -> Tuple[bool, str, int]:
    """
    Check if a URL is accessible.

    Returns:
        Tuple of (accessible: bool, status: str, response_time_ms: int)
    """
    import time

    try:
        # Create SSL context that doesn't verify certificates (for checking availability only)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        # Set up request with realistic headers
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )

        start_time = time.time()

        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as response:
            elapsed_ms = int((time.time() - start_time) * 1000)
            status_code = response.getcode()

            if status_code == 200:
                return (True, "OK", elapsed_ms)
            else:
                return (True, f"HTTP {status_code}", elapsed_ms)

    except urllib.error.HTTPError as e:
        elapsed_ms = int((time.time() - start_time) * 1000)
        # Some HTTP errors still mean the service is accessible
        if e.code in [301, 302, 303, 307, 308, 403, 401]:
            return (True, f"HTTP {e.code}", elapsed_ms)
        return (False, f"HTTP {e.code}", elapsed_ms)

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            return (False, "Timeout", timeout * 1000)
        return (False, f"Connection Error", 0)

    except socket.timeout:
        return (False, "Timeout", timeout * 1000)

    except Exception as e:
        return (False, f"Error: {type(e).__name__}", 0)


def format_status(accessible: bool, status: str) -> str:
    """Format status with color indicators."""
    if accessible:
        return f"✓ {status}"
    else:
        return f"✗ {status}"


def print_table_header():
    """Print table header."""
    print("\n" + "="*80)
    print(f"{'Service':<25} {'URL':<35} {'Status':<20}")
    print("="*80)


def print_table_row(name: str, url: str, accessible: bool, status: str, response_time: int):
    """Print a table row."""
    status_str = format_status(accessible, status)
    time_str = f"({response_time}ms)" if accessible else ""
    print(f"{name:<25} {url:<35} {status_str:<20} {time_str}")


def check_services(services: Dict[str, List[Tuple[str, str]]], verbose: bool = True) -> Dict:
    """
    Check all services and return results.

    Args:
        services: Dictionary of service categories and their URLs
        verbose: Print progress information

    Returns:
        Dictionary with results
    """
    results = {}
    total_checked = 0
    total_accessible = 0

    for category, service_list in services.items():
        if verbose:
            print(f"\n{'='*80}")
            print(f"Category: {category}")
            print_table_header()

        category_results = []

        for service_name, service_url in service_list:
            if verbose:
                print(f"Checking {service_name}...", end="\r")

            accessible, status, response_time = check_url(service_url)

            category_results.append({
                "name": service_name,
                "url": service_url,
                "accessible": accessible,
                "status": status,
                "response_time_ms": response_time
            })

            if verbose:
                print_table_row(service_name, service_url, accessible, status, response_time)

            total_checked += 1
            if accessible:
                total_accessible += 1

        results[category] = category_results

    return {
        "results": results,
        "summary": {
            "total_checked": total_checked,
            "total_accessible": total_accessible,
            "accessibility_rate": f"{(total_accessible/total_checked)*100:.1f}%"
        }
    }


def print_summary(summary: Dict):
    """Print summary statistics."""
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total services checked: {summary['total_checked']}")
    print(f"Accessible services: {summary['total_accessible']}")
    print(f"Accessibility rate: {summary['accessibility_rate']}")
    print("="*80)


def print_recommendations(results: Dict):
    """Print recommendations based on results."""
    print("\n" + "="*80)
    print("RECOMMENDATIONS")
    print("="*80)

    # Check phone services
    phone_results = results.get("Virtual Phone Numbers", [])
    accessible_phone = [s["name"] for s in phone_results if s["accessible"]]

    if "TextNow" in accessible_phone:
        print("✓ TextNow is accessible - You can use free US phone numbers")
    elif "Twilio" in accessible_phone:
        print("✓ Twilio is accessible - Recommended for developer use")
    else:
        print("⚠ Major phone services may be blocked - Consider using VPN")

    # Check card services
    card_results = results.get("Virtual Credit Cards", [])
    accessible_cards = [s["name"] for s in card_results if s["accessible"]]

    if "WildCard" in accessible_cards:
        print("✓ WildCard is accessible - Good option for Chinese users")
    elif "Depay" in accessible_cards:
        print("✓ Depay is accessible - Good option for crypto users")
    elif "Revolut" in accessible_cards or "Wise" in accessible_cards:
        print("✓ Revolut/Wise accessible - Use if you have residency")
    else:
        print("⚠ Virtual card services may be blocked - VPN recommended")

    # Check AI services
    ai_results = results.get("AI Services", [])
    accessible_ai = [s["name"] for s in ai_results if s["accessible"]]

    if "Claude" in accessible_ai:
        print("✓ Claude is accessible - You can subscribe directly")
    elif "GitHub" in accessible_ai:
        print("✓ GitHub is accessible - You can use GitHub Copilot")
    else:
        print("⚠ AI services may be restricted - Check regional availability")

    print("="*80)


def save_json_report(results: Dict, filename: str = "service_check_results.json"):
    """Save results to JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Results saved to {filename}")
    except Exception as e:
        print(f"\n✗ Failed to save results: {e}")


def main():
    """Main function."""
    print("="*80)
    print("Service Availability Checker")
    print("Checking access to virtual phone and card services...")
    print("="*80)
    print("\nNote: This checks basic connectivity only.")
    print("Accessibility doesn't guarantee service works in your region.")
    print("Some services may require VPN or have regional restrictions.")

    # Check all services
    results = check_services(SERVICES, verbose=True)

    # Print summary
    print_summary(results["summary"])

    # Print recommendations
    print_recommendations(results["results"])

    # Offer to save results
    print("\n" + "="*80)
    save_choice = input("Save results to JSON file? (y/n): ").strip().lower()
    if save_choice == 'y':
        save_json_report(results)

    print("\n" + "="*80)
    print("Check complete!")
    print("\nFor detailed setup instructions, see REPORT.md")
    print("For quick start guide, see README.md")
    print("="*80)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Check cancelled by user")
        exit(1)
    except Exception as e:
        print(f"\n\n✗ Error: {e}")
        exit(1)
