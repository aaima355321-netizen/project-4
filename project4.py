# Project 4: System Vulnerability Checklist
# System Vulnerability Assessment

print("======================================")
print("     SYSTEM VULNERABILITY CHECKLIST")
print("======================================")

vulnerabilities = 0

# 1. Check Password
print("\n1. Password Security")
password = input("Enter your password to check its strength: ")

if len(password) < 8:
    print("❌ Weak Password: Password should contain at least 8 characters.")
    vulnerabilities += 1
else:
    has_digit = False
    has_upper = False
    has_lower = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True

    if has_digit and has_upper and has_lower:
        print("✅ Strong Password")
    else:
        print("⚠️ Password needs improvement.")
        print("Use uppercase, lowercase, and numbers.")
        vulnerabilities += 1


# 2. Check Software Updates
print("\n2. Software Update Status")
update = input("Is your software updated? (yes/no): ").lower()

if update == "yes":
    print("✅ Software is up to date.")
else:
    print("❌ Software is not updated.")
    print("Recommendation: Install the latest security updates.")
    vulnerabilities += 1


# 3. Check Unsafe Practices
print("\n3. Security Practices")

unknown_links = input(
    "Do you open links from unknown sources? (yes/no): "
).lower()

if unknown_links == "yes":
    print("❌ Unsafe Practice: Avoid unknown links.")
    vulnerabilities += 1
else:
    print("✅ Good practice: You avoid unknown links.")


# 4. Check Antivirus
print("\n4. Antivirus Protection")

antivirus = input(
    "Do you have antivirus/security protection enabled? (yes/no): "
).lower()

if antivirus == "yes":
    print("✅ Security protection is enabled.")
else:
    print("❌ No security protection detected.")
    print("Recommendation: Enable trusted security software.")
    vulnerabilities += 1


# Final Risk Assessment
print("\n======================================")
print("        VULNERABILITY REPORT")
print("======================================")

print("Total vulnerabilities found:", vulnerabilities)

if vulnerabilities == 0:
    print("🟢 Risk Level: LOW")
    print("Your system follows basic security practices.")

elif vulnerabilities <= 2:
    print("🟡 Risk Level: MEDIUM")
    print("Some security improvements are required.")

else:
    print("🔴 Risk Level: HIGH")
    print("Your system has several basic security weaknesses.")

print("\nRecommendations:")
print("- Use strong passwords.")
print("- Keep software updated.")
print("- Avoid unknown links.")
print("- Enable security/antivirus protection.")

print("\n======================================")
print("       Assessment Completed")
print("======================================")