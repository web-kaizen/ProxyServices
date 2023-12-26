from django.db import models


class LogModel(models.Model):

    """PROXY FIELDS"""
    proxy_method = models.CharField(max_length=10, null=True, blank=True)
    proxy_url = models.URLField(max_length=255, null=True, blank=True)
    proxy_request_headers = models.JSONField(null=True, blank=True)
    proxy_request_body = models.TextField(null=True, blank=True)

    """CORE FIELDS"""
    core_url = models.URLField(max_length=255, null=True, blank=True)
    core_response_headers = models.JSONField(null=True, blank=True)
    core_response_body = models.TextField(null=True, blank=True)
    core_response_status_code = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
