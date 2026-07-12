from django.db import models


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    category = models.ForeignKey('category', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name   
    
class section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class StockOut(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_of_issue = models.DateField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    section = models.ForeignKey(section, on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=250, null=True)
    remarks = models.TextField()

    def __str__(self):
        return self.item.name
    

class StockIn(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_of_entry = models.DateField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    reciever = models.CharField(max_length=250)
    remarks = models.TextField()

    def __str__(self):
        return self.item.name

   