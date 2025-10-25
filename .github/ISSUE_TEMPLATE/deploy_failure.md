---
name: Deploy Failure
about: Report a deployment failure for investigation and remediation
title: '[DEPLOY FAILURE] '
labels: ['deploy-failure', 'urgent']
assignees: ''
---

## Deployment Failure Summary

**Date/Time of Failure:** 
**Environment:** (e.g., production, staging)
**Deployment ID/Run:** 
**Commit SHA:** 

## Description of Failure

Provide a clear and concise description of what went wrong during the deployment:



## Observed Symptoms

Describe what happened (check all that apply):
- [ ] Build failed
- [ ] Tests failed
- [ ] Deployment to platform failed
- [ ] Post-deployment health checks failed
- [ ] Service unavailable after deployment
- [ ] Other (describe below)



## Deployment Logs

Please attach or paste relevant logs from:
- **Build logs:**
```
[Paste build logs here]
```

- **Deployment logs:**
```
[Paste deployment logs here]
```

- **Application logs (if applicable):**
```
[Paste application logs here]
```

## Error Messages

Include any specific error messages encountered:
```
[Paste error messages here]
```

## Remediation/Triage Steps

### Immediate Actions
1. **Check deployment status:**
   - Verify the deployment run in Railway/GitHub Actions
   - Review logs for specific error messages
   - Check service health endpoints

2. **Assess impact:**
   - Is the service currently down?
   - Are users affected?
   - Is a rollback needed immediately?

3. **Quick fixes to try:**
   - Re-run the deployment if it was a transient failure
   - Check for environment variable changes
   - Verify secrets and credentials are valid

### Investigation Steps
1. **Review recent changes:**
   - Check the commit that triggered the failure
   - Review recent PRs merged before the failure
   - Look for dependency updates or configuration changes

2. **Check dependencies:**
   - Verify all external services are operational
   - Check Railway platform status
   - Verify database connections and migrations

3. **Test locally:**
   - Pull the failed commit and test locally
   - Run tests in CI environment
   - Check for environment-specific issues

### Resolution Actions
- [ ] Root cause identified (document below)
- [ ] Fix implemented and tested
- [ ] Successful deployment completed
- [ ] Post-deployment verification passed
- [ ] Incident report created (if applicable)

## Root Cause Analysis

Once identified, document the root cause:



## Additional Context

Add any other context, screenshots, or information that may help diagnose the issue:



## Related Issues/PRs

- Related to #
- Caused by PR #
