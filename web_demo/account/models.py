from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # 产品名称
    description = models.TextField()         # 产品描述
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 产品价格
    quantity = models.IntegerField()         # 产品数量
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return self.name
