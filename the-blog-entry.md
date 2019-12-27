# Didactic Engine Flask

I've worked with Python almost entirely from the maintenance programmer perspective. That is, I take other code written already, make edits, add features, and then redeploy it. I've created exactly zero greenfield applications in Python. That changes today however, with the creation of the didactic-engine-flask app!

## Prerequisites

The only prereq to understanding this article is knowing git, understanding programming in general, and that should be enough. I'm starting this from ground zero. If you're just getting started with Python, be sure to read "[Getting Started With Python Right!](https://compositecode.blog/2019/12/23/getting-started-with-python-right/)" and "[Unbreaking Python Through Virtual Environments](https://compositecode.blog/2019/12/25/unbreaking-python-through-virtual-environments/)" about setting up your environment. These two entries cover enough to ensure you won't end up with broken, conflicted, and convoluted Python environments.

## Mission: Build a Flask based API.

This post is about a singular thing, building an API with Flask. It won't be about data modeling, databases, or wrapping middleware into the fold. It's pure and simple Flask, with just the bare necessities needed to get an API working and responding appropriately requests.

Flask is almost perfect for an example this this because it is a very focused framework. Flask is considered a *microframework*, which fits the mission of this post, as the *micro* in *microframework* is focused on keeping the core simple but extensible. Flask doesn't have tons of convention nor has it pre-made decisions inherent in the framework such as which database or other matters of that sort. The decisions, becasuse of the nature of the framework, are easy to made by us users of the framework because of this core focus.

There are however a few conventions or defaults used in initial configuration of the framework. Templates and static files are stored in subdirectories within the app source tree. The names (by convention) are *templates* and *state*. This can be changed, but these upfront conventions really don't need to be and we can skip over that and get to more important things.

## Flask Installation



Thanks to [@tlockney](https://twitter.com/tlockney), [@mbbroberg](https://twitter.com/mbbroberg), and [Moshe Zadka](https://twitter.com/moshezadka) so far for ideas around posts, using Python right, and better ways to do things. Watch out, this list could get huge!