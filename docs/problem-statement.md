# AI IT Support Automation Platform: Problem Statement

**Project:** AI IT Support Automation Platform
**Author:** Zamzam
**Document:** `docs/problem-statement.md`

## 1. Business Problem

A hypothetical company with 150 employees and two IT technicians experiences delays in responding to employee IT support requests.

These delays may cause employee frustration, interruptions to work, and additional pressure on the IT team.

The company needs a faster, secure, and reliable way to receive, organize, troubleshoot, and escalate IT support requests.

## 2. Proposed Solution

Develop an AI-assisted IT Support Automation Platform that automates ticket intake, classification, and routing while providing approved troubleshooting guidance.

The system will escalate sensitive, complex, or unresolved issues to human technicians.

## 3. Initial Supported IT Problems

| Problem | Example | First diagnostics |
|---|---|---|
| Company portal | An employee cannot load or access the company website. | DNS lookup, port 443 check, and HTTP status check (`scripts/health_check.py`) |
| VPN connectivity | An employee cannot connect to the company's VPN. | DNS lookup and reachability checks to the VPN server |
| Email problems | An employee cannot send email or log in to their email account. | Read-only account and sign-in status in Microsoft 365 (assumes the company uses Microsoft 365) |

## 4. Users

- Employees submitting IT support requests.
- IT technicians investigating and resolving issues.
- IT managers monitoring support performance.
- Authorized personnel approving sensitive actions.

## 5. Security and Automation Boundaries

The platform may perform authorized, read-only diagnostics and automate tested routine operations such as creating tickets and sending notifications.

Privileged actions, including changing account permissions or resetting passwords, require appropriate human authorization and approval.

Every automated action and every human approval is recorded in an audit log.

The initial learning system will use synthetic data and simulated infrastructure. Autonomous privileged changes to real company systems are outside its scope.

## 6. Success Measures

We will evaluate the platform using three KPIs:

| KPI | What it measures | How it is measured |
|---|---|---|
| Average first-response time | Whether employees receive meaningful responses faster | Time from ticket submission to the first reply that contains a diagnosis or next step. Automatic acknowledgements do not count. |
| Ticket resolution rate | The percentage of tickets successfully resolved | Tickets closed and not reopened within 7 days, divided by all tickets |
| Human escalation rate | Whether routine issues need technician involvement less often, without compromising resolution quality or safety | Routine tickets escalated, divided by all routine tickets. Sensitive issues (security incidents, account permission changes, password resets) must always escalate: target 100%. |

Actual improvement targets will be established after measuring the starting performance.

## 7. Intended Outcome

The platform should help employees receive faster IT support, reduce unnecessary repetitive work for technicians, and maintain secure, reliable human oversight of sensitive operations.