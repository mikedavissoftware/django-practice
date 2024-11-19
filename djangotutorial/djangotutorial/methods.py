### MODEL-SPECIFIC

# GET - index
ModelName.objects.all()

# GET - singular
Model.objects.get() - get

# Model.objects.filter() - get filtered selection
# Model.objects.exclude() - get with exclusion
# Model.objects.order_by() - get 
# Model.objects.create() - create instance & save it to DB
# instance.save() - save or update instance
# Model.objects.filter().update() - update filtered selection
# instance.delete() - delete instance
# Model.objects.filter().delete() - delete filtered selection
# Model.objects.
# Model.objects.
# Model.objects.any_custom_method(parameter1=value1, parameter2=value2)

# .save() saves to database
# .create() create and save

# LOOKUPS https://www.w3schools.com/django/django_ref_field_lookups.php
# __contains
# __icontains (case insensitive)
# __endswith
# __iendswith (case ins.)
# __startswith
# __istartswith (case ins.)
# __exact
# __iexact (case ins.)
# __in (matches one of the values)
# __isnull

# __date
# __year
# __iso_year (minimum four digit YYYY)
# __quarter (matches quarter of the year)
# __month
# __week (of the year; 1-53)
# __week_day (sunday is 1)
# __iso_week_day (monday is 1)
# __day (day of the month)
# __time
# __hour
# __minute
# __second

# __range (between __range(low-val, hi-val))
# __gt (greater than)
# __gte (gt or equal to)
# __lt (less than)
# __lte (lt or equal to)