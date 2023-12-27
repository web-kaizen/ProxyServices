from django.db import models


class LogModel(models.Model):
    """From Client to Proxy fields"""
    client_request_method = models.CharField(max_length=10, null=True, blank=True)
    client_request_url = models.URLField(max_length=255, null=True, blank=True)
    client_request_headers = models.TextField(null=True, blank=True)
    client_request_body = models.TextField(null=True, blank=True)

    """From Proxy to Yadro fields"""
    proxy_request_method = models.CharField(max_length=10, null=True, blank=True)
    proxy_request_url = models.URLField(max_length=255, null=True, blank=True)
    proxy_request_headers = models.TextField(null=True, blank=True)
    proxy_request_body = models.TextField(null=True, blank=True)

    """From Yadro to Proxy fields"""
    core_response_headers = models.TextField(null=True, blank=True)
    core_response_body = models.TextField(null=True, blank=True)
    core_response_status_code = models.PositiveIntegerField(null=True, blank=True)

    """From Proxy to Client Fields"""
    proxy_response_headers = models.TextField(null=True, blank=True)
    proxy_response_body = models.TextField(null=True, blank=True)
    proxy_response_status_code = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (f'ID: {self.id} | '
                f'Client request method: {self.client_request_method} | '
                f'Proxy response status code: {self.proxy_response_status_code}')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
