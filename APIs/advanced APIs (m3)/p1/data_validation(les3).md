# 📑 Data Validation
- 💡DRF provide different features we can use it 


## Method 1 ( Conditions in the fields )
```python
price = serializers.DecimalField(max_digits=6,decimal_places=2,min_value=2)

# this ensure the value sholud be above 2
```
## Method 2 ( using Keywords arguments in Meta class )
```python 
class Meta:
    model = MenuItem
    fields = ['id','title','price','stock']
    extra_kwargs = {
        'price':{'min_value':2},
        'stock':{'min_value':0},
    }

# here we can validate multiple fields    
```   
## Method 3 ( using validate_field() method )
- 💡we can replace `field` with actual field name
```python
# above Meta class
def validate_price(self,value):
    if value < 2:
        raise serializers.ValidationError('price should be above 2')

def validate_stock(self,value):
    if value < 0:
        raise serializers.ValidationError('stock should be above 0')

```
## Method 4 ( using validate() method )
- 💡here we can validate multiple values at once
- 💡DRF will pass all the input values to this method
```python
def validate(self,attrs):
    if (attrs['price'] < 2):
        raise serializers.ValidationError('price should be above 2')
    if(attrs['stock'] < ):
        raise serializers.ValidationError('stock should be above 0')
    return super().validate(attrs)    
```

## 📑Unique validation
- 💡this case, we make sure that there is no duplicate entry from clients.
- 💡that ensure the uniqueness of a single field or combination of fields.
- 💡`UniqueValidator` is class to validate the uniqueness of field.
- 💡`UniqueTogetherValidator` make it for combination of fields.

## 📑How to use `UniqueValidator`
```python
from rest_framework.validators import UniqueValidator
# in extra_kwargs
extra_kwargs = {
    'title':{
        'validators':[
            UniqueValidator(
                queryset=MenuItem.objects.all(),
            ),
        ]
    }
}

# or we can add it when declaring field above Meta class
title = serializers.CharField(
    max_length=255,
    validators=[UniqueValidator(queryset=MenuItem.objects.all())],
)
```

## 📑How to use `UniqueTogetherValidator`
```python
validators = [
    UniqueTogetherValidator(
        queryset=MenuItem.objects.all(),
        fields=['title','price'],
        ),
]
```