# A calzone explains Python's method resolution order better than the docs

Conf42 Blog, 2021-05-26. https://www.conf42.com/blog/python2021/python-c3-mro-mixins-calzone

In short: Jason C. McDonald (MousePaw Media) at Conf42 Python 2021 on how the C3 MRO resolves multiple inheritance and how to use it for mixins

Multiple inheritance in Python is not the horror story other languages make it out to be, as long as you know the one algorithm that decides which method runs. At Conf42 Python 2021, Jason C. McDonald, CEO of MousePaw Media and author of Dead Simple Python (No Starch Press), walks through the C3 method resolution order with food emoji, then puts it to work with mixins in a live-coded diner and coffee shop.

The talk is short, practical and aimed at anyone who has ever stared at a class hierarchy and asked why that particular `eat()` got called.

## Which method gets called when two parents define it?

He opens with the classic setup: class C inherits from A and B, both define the same method, and both share a parent that defines it too. That is the diamond, which he notes Java folks know as the deadly diamond of death, and the reason many language designers simply refuse to support multiple inheritance.

Python answers the question with the C3 MRO, which, Jason C. McDonald said at Conf42 Python 2021, "frankly sounds like a droid out of Star wars." Its job is to compute the superclass linearization of a class: an ordered list Python walks left to right, stopping at the first class that has the method.

## How the C3 merge actually works

The walkthrough builds up from `Food` (linearization: Food, object), through `Pizza` and `Sandwich` (each: itself, Food, object), to a `Calzone` that inherits from both Pizza and Sandwich. The merge rule is a single sentence: take the leftmost head of the lists being merged, and bring it in only if it does not appear in the tail of any other list. If it does, try the next head.

For the calzone that gives Calzone, Pizza, Sandwich, Food, object. Food can't come in right after Pizza because it still sits in Sandwich's tail, so Sandwich jumps the queue. The practical upshot: call `eat()` on a calzone and you get Pizza's version. Sandwich's is never reached. Inheritance order is not cosmetic.

## Where it blows up, and the cheap fix

Then the fun part. A `PizzaSandwich` (the cold leftover breakfast he describes with real affection) inherits from Sandwich and then Pizza, the opposite order. A `CalzonePizzaSandwich` that inherits from both Calzone and PizzaSandwich hits an impasse: Pizza is blocked by one list's tail, Sandwich by the other's, and Python raises `TypeError: Cannot create a consistent method resolution`.

The fix in this case is to make the orders agree: have PizzaSandwich inherit from Pizza, then Sandwich, like Calzone does. He is careful to say this is not a strategy for complex hierarchies, where you have to actually work it out, and points to Raymond Hettinger's article "Super Considered Super!" for the advanced patterns. When you need a specific parent's method regardless of the MRO, call it on the class and pass `self` explicitly, as in `Pizza.eat(self)`.

## Mixins: composition that happens to use inheritance

The second half is where the theory pays off. A diner and a coffee shop are both restaurants, but neither is a kind of the other. Both need a short order cook; only the coffee shop has a barista. Each staff member needs restaurant data (orders, recipes) and makes no sense on their own.

That is the mixin: a class that contributes methods or attributes, may rely on attributes of the class using it, and isn't meant to stand alone. "A mix in is technically a form of composition. It's just a form of composition that happens to use inheritance as the means of composing," Jason C. McDonald said at Conf42 Python 2021. A diner has a short order cook; it is not one.

He live-codes it with Click: a `restaurant` CLI with `diner` and `coffeeshop` commands, a `ShortOrderCookMixin` with `cook()` and a plain `brew()` that pours drip coffee whatever you ask for, and a `BaristaMixin` with a proper `brew()`. Both expect a `self.ready` dict on the host class, which he documents in the mixin's docstring and recommends you always do.

## The bug that proves the point

The coffee shop inherits ShortOrderCookMixin first, then BaristaMixin. Order a cappuccino and you get drip coffee, because the MRO finds the cook's `brew()` first. Two fixes: swap the inheritance order, or define `brew()` on the coffee shop and call `BaristaMixin.brew(self, ...)` explicitly, which works even when you can't change the order. Same lesson as the calzone, now with a real symptom.

His closing caveats are sensible: not everything that looks like a nail is a nail, mixins can complicate code, and multiple inheritance plus abstract base classes (or metaclasses) gets interesting fast.

## Who should watch

Python developers who use classes daily but have never traced an MRO by hand, and anyone who's met that TypeError and moved classes around until it went away. The code is on GitHub at codemouse92/WhoseMethod.

## Related Conf42 talks

- Eti Ijeoma on [Python dunder methods](https://www.conf42.com/Python_2025_Eti_Ijeoma_python_dunder_methods) at Conf42 Python 2025.
- Tiago Bacciotti Moreira on [an OOP teaching tool](https://www.conf42.com/Python_2022_Tiago_Bacciotti_Moreira_oop_teaching_tool_in_the_Information_systems_course) at Conf42 Python 2022.
- Cheuk Ting Ho on [how to be Pythonic](https://www.conf42.com/Python_2021_Cheuk_Ting_Ho_how_to_be_pythonic_query_language), from the same event.

[Watch Jason C. McDonald's talk](https://www.conf42.com/Python_2021_Jason_C_McDonald_Whose_Method_Is_It_Anyway) from [Conf42 Python 2021](https://www.conf42.com/python2021).

## From MousePaw Media

MousePaw Media is the company Jason C. McDonald leads as CEO.

- MousePaw Media: [mousepawmedia.com](https://mousepawmedia.com/)

[Watch the talk on YouTube](https://youtu.be/svo8rcU-Q5Q).

## Watch the talk

[Whose Method Is It Anyway?](https://www.conf42.com/Python_2021_Jason_C_McDonald_Whose_Method_Is_It_Anyway) at Conf42 Python 2021.
