from django.db import models

class NetworkTraffic(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    src_ip = models.CharField(max_length=100)
    dst_ip = models.CharField(max_length=100)
    protocol = models.CharField(max_length=50)
    length = models.IntegerField()

    def __str__(self):
        return f"{self.src_ip} -> {self.dst_ip} ({self.protocol})"
