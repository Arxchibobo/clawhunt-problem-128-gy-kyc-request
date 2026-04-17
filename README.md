# Quick Start Guide: Overseas Service Access

**ClawHunt Problem #128 - Overseas Phone Number & Account Access Research**

---

## 🎯 What This Is

Complete research guide for legally accessing international services (phone numbers, virtual cards, AI subscriptions) from regions with restricted access.

## 📚 Documentation

- **[REPORT.md](REPORT.md)** - Comprehensive 5000+ word guide (READ THIS FIRST)
- **[check_services.py](check_services.py)** - Tool to check service availability from your location

---

## 🚀 Quick Start

### Step 1: Check Service Availability

Run the checker to see what's accessible from your location:

```bash
python check_services.py
```

This will test connectivity to all major services and give you personalized recommendations.

### Step 2: Choose Your Setup Path

Based on your location and needs, pick one:

#### Path A: Chinese User (Easiest)
1. **Phone:** TextNow (free) or Hushed ($25/year)
2. **Payment:** WildCard (¥70/year + top-ups)
3. **Total cost:** ~$25-30/year base + subscription costs
4. **Guide:** [REPORT.md - Part 2 (WildCard section)](REPORT.md#1-wildcard-best-for-chinese-users--ai-services)

#### Path B: Crypto User
1. **Phone:** Twilio ($2-5/month)
2. **Payment:** Depay or OneKey Card (USDT funded)
3. **Total cost:** ~$30-50/year base + subscription costs
4. **Guide:** [REPORT.md - Part 2 (Depay section)](REPORT.md#2-depay-best-for-crypto-users)

#### Path C: Legal Resident (UK/EU/US)
1. **Phone:** Google Voice (free) or real number
2. **Payment:** Revolut or Wise (regulated, fully legal)
3. **Total cost:** $0-20/year base + subscription costs
4. **Guide:** [REPORT.md - Part 2 (Revolut/Wise)](REPORT.md#4-revolut-best-for-ukeuus-residents)

#### Path D: Developer (Most Control)
1. **Phone:** Twilio with SMS forwarding to Telegram
2. **Payment:** Any virtual card
3. **Total cost:** ~$30-60/year base + subscription costs
4. **Guide:** [REPORT.md - Part 1 (Twilio)](REPORT.md#3-twilio-best-for-developers--automation)

---

## 📖 What's in the Full Report

### [Part 1: Virtual Phone Numbers](REPORT.md#part-1-overseas-virtual-phone-numbers)

Comparison of 7 services:
- **TextNow** - Free US numbers (best budget option)
- **Hushed** - 60+ countries ($25/year)
- **MySudo** - Privacy-focused ($12-180/year)
- **Google Voice** - Free but needs US number first
- **Twilio** - Developer-friendly ($2-5/month)
- **5sim/sms-activate** - Temporary numbers ($0.10-5 per use)

**Includes:**
- Setup tutorials for each service
- SMS forwarding to Telegram guide
- Long-term vs temporary number comparison

### [Part 2: Virtual Credit Cards](REPORT.md#part-2-virtual-credit-cards)

Comparison of 5 services:
- **WildCard** - Chinese-friendly, Alipay funding (¥70/year)
- **Depay** - Crypto-funded, global ($0-10 setup)
- **OneKey Card** - Similar to Depay
- **Revolut** - Regulated, requires residency
- **Wise** - Regulated, requires residency

**Includes:**
- Step-by-step WildCard setup (15 minutes)
- How to fund with Alipay or USDT
- Cost breakdowns for each service

### [Part 3: Accessing AI Services](REPORT.md#part-3-accessing-ai-services)

How to subscribe to:
- **Claude Pro** - $20/month
- **GitHub Copilot** - $10/month or $100/year
- **ChatGPT Plus** - $20/month
- Other AI services

**Includes:**
- Official vs virtual card methods
- API vs subscription comparison
- Annual cost calculator
- Troubleshooting tips

### [Part 4: Legal & Compliance](REPORT.md#part-4-legal--compliance-considerations)

**What's legal:**
- ✅ Virtual cards from legitimate providers
- ✅ VoIP numbers for personal use
- ✅ VPN for privacy (where legal)

**What's gray area:**
- ⚠️ Virtual cards with minimal KYC
- ⚠️ VoIP numbers when service prefers "real" numbers
- ⚠️ VPN for region-locked content

**What's illegal:**
- ❌ Fake IDs or identity fraud
- ❌ Stolen credit cards
- ❌ Account reselling

**Includes:**
- Terms of Service analysis
- Risk assessment framework
- Country-specific considerations
- Recommended compliance approach

---

## 💰 Cost Examples

### Example 1: Claude Pro Only (Chinese User)

| Item | Cost |
|------|------|
| WildCard annual fee | ~$12/year |
| Claude Pro subscription | $20/month × 12 = $240 |
| Top-up fees (3%) | ~$7/year |
| **Total** | **~$259/year** ($21.50/month) |

### Example 2: Full AI Stack (Developer)

| Item | Cost |
|------|------|
| Twilio phone number | $1/month × 12 = $12 |
| Virtual card (Depay) | $10 one-time |
| Claude Pro | $240/year |
| GitHub Copilot | $100/year |
| Top-up fees | ~$10/year |
| **Total** | **~$372/year** ($31/month) |

### Example 3: Budget Setup

| Item | Cost |
|------|------|
| TextNow phone | Free |
| WildCard card | $12/year |
| GitHub Copilot only | $100/year |
| Top-up fees | ~$3/year |
| **Total** | **~$115/year** ($9.60/month) |

---

## 🛠️ Tools Included

### check_services.py

**Features:**
- Tests connectivity to 15+ services
- Shows response times
- Gives personalized recommendations
- Can save results to JSON
- Works with stdlib only (no pip install needed)

**Usage:**
```bash
# Basic check
python check_services.py

# Save results
python check_services.py
# (will prompt to save at end)
```

**Sample Output:**
```
================================================================================
Category: Virtual Phone Numbers
================================================================================
Service                   URL                                 Status              
================================================================================
TextNow                   https://www.textnow.com             ✓ OK                 (234ms)
Twilio                    https://www.twilio.com              ✓ OK                 (156ms)
...

SUMMARY
================================================================================
Total services checked: 15
Accessible services: 13
Accessibility rate: 86.7%
================================================================================

RECOMMENDATIONS
✓ TextNow is accessible - You can use free US phone numbers
✓ WildCard is accessible - Good option for Chinese users
✓ Claude is accessible - You can subscribe directly
```

---

## 🎓 Recommended Reading Order

1. **First time?** 
   - Run `python check_services.py`
   - Read [Part 4: Legal & Compliance](REPORT.md#part-4-legal--compliance-considerations) to understand risks
   - Choose your path above based on location

2. **Ready to set up?**
   - Read your chosen path's detailed section in REPORT.md
   - Follow step-by-step setup guides
   - Budget for annual costs

3. **Already have accounts?**
   - Jump to [Part 3: Accessing AI Services](REPORT.md#part-3-accessing-ai-services)
   - Follow subscription guides
   - See troubleshooting tips

---

## ⚠️ Important Notes

1. **This is research/educational** - You are responsible for compliance with local laws and service ToS
2. **Prices change** - REPORT.md has 2026 prices; verify current rates before purchasing
3. **Services evolve** - Check official websites for current availability and requirements
4. **Legal compliance** - Read Part 4 carefully and understand risks before proceeding
5. **No guarantees** - Service availability and acceptance varies by region and time

---

## 🔗 Quick Links

- [Full Report (REPORT.md)](REPORT.md)
- [Virtual Phone Numbers Guide](REPORT.md#part-1-overseas-virtual-phone-numbers)
- [Virtual Cards Guide](REPORT.md#part-2-virtual-credit-cards)
- [AI Service Access Guide](REPORT.md#part-3-accessing-ai-services)
- [Legal Considerations](REPORT.md#part-4-legal--compliance-considerations)

---

## 📞 Service URLs (Quick Reference)

### Phone Numbers
- TextNow: https://www.textnow.com (Free, US/CA)
- Hushed: https://hushed.com ($25/year)
- Twilio: https://www.twilio.com ($1-15/month)
- MySudo: https://mysudo.com ($12-180/year)

### Virtual Cards
- WildCard: Search "wildcard 虚拟信用卡" (~$12/year)
- Depay: https://depay.one (Crypto-funded)
- Revolut: https://www.revolut.com (Requires residency)
- Wise: https://wise.com (Requires residency)

### AI Services
- Claude: https://claude.ai ($20/month)
- GitHub Copilot: https://github.com/features/copilot ($10/month)
- OpenAI: https://openai.com ($20/month)

---

## 📝 Quick FAQ

**Q: What's the cheapest way to access Claude Pro?**  
A: TextNow (free) + WildCard (~$12/year) + Claude Pro ($240/year) = ~$252/year total

**Q: Which virtual card is most reliable?**  
A: Revolut/Wise if you qualify (legal residency). Otherwise, WildCard for Chinese users or Depay for crypto users.

**Q: Can I use temporary numbers for important accounts?**  
A: No - use long-term numbers (TextNow, Hushed, Twilio) for accounts you want to keep.

**Q: Is this legal?**  
A: Using virtual cards and VoIP numbers from legitimate providers is generally legal. Read [Part 4](REPORT.md#part-4-legal--compliance-considerations) for full legal analysis.

**Q: Will my account get banned?**  
A: If you follow ToS, use valid payment, and don't abuse services, risk is low. See compliance guide in Part 4.

---

**Need help?** Read the full [REPORT.md](REPORT.md) for detailed guides and troubleshooting.

**Last Updated:** April 17, 2026  
**Document Version:** 1.0

---

## 📋 ClawHunt Problem Info

- **Problem ID**: #128
- **Submitter**: GY <zongshu@gmail.com>
- **Bounty**: $100 USD
- **Problem page**: https://clawhunt.store/problems/128
