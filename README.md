# APIs (Application Programming Interface)
##### February 22, 2018
###

### API Overview
APIs are a term that gets thrown around a lot in the software world. The best way to think of them is a *gate* to data (in our case). They can also be 'gates' to software and other tools or resources.

APIs are a way to give outside users access to specific segments of your technology. Businesses often use *Web APIs* to give developers access to non-critical datasets that they can makes 'calls' to. 

Python is almost always included in API deployment because of the ubiquity(sp?) of Python. You'll also see deployments for Ruby, JS, or even C++. But almost none as often as Python. 

### How do we interact with Web APIs

The first step is to get a *protected key*, which is a alpha-numeric string that in personal to you, and gives you access to select resources, but also constrains the number of requests you can make(usually a very high nuber that we wouldn't get close to touching. ex: Etsy's API is 5/second or 5k per day)

Once we have the *key*, we include it in our python script, based on the Web APIs example use cases(typically in the 'developer' section of their website).

We then make a *HTTP* request that returns a data object, formatted in *XML*(Extensible Markup Language) think web `<sale_amount>12.00<sale_amount/>` or *JSON*(Java SCript Object Notation) - think a Python Dictionary: `"sale_amount":"12.00"`

We use the *requests* module to make the actual HTTP request, and *bs4* (beautiful soup) to parse through the response that is returned to us.

### Some cool APIs:

