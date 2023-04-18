# ai-exercise

This project uses OpenAI’s API to
1. summarize and interpret error logs
2. fill out a new Github issue markdown based on [this template](https://github.com/stevemao/github-issue-templates/blob/master/questions-answers/ISSUE_TEMPLATE.md).
3. file the Github Issue using Github's API as a new issue in this project
 
The inspiration comes from real experiences of investigating developer issues and escalating the problem to the appropriate engineering team in Jira. This project should automate some of these tasks for simple bugs. At the very least, it gives Support Engineers a template to streamline creating issues. This enables Support Engineers to more efficiently draft and create Issues that need to be addressed. It can also help suggest where the problems occur and what potential steps users can do to address the issue.

I used ChatGPT for all stages of the project, from
1. creating a simple Python Hello World web application
2. writing a function to create a Github issue
3. writing a function to call the OpenAI API. However, since ChatGPT was trained before the new `gpt-3.5-turbo` model was released, I needed to update the API call from the Python SDK to account for the model difference.

I used ChatGPT to prototype with some samples logs from https://github.com/logpai/loghub. Then ran the same sequence in the playground by writing a script. ChatGPT was used in writing the code. I primarily triggered the service using the [./py/test.py](test python script) to post to my endpoint. This was also written mainly by ChatGPT.

# Results

This project has [several issues filed](https://github.com/valeriec0/ai-exercise/issues). Every issue was created using the OpenAI API output. The more recent ones are using `gpt-3.5-turbo` and the older ones are using `davinci` because that is what ChatGPT originally suggested.

# Future

A future extension of this project that I could not finish using just ChatGPT is build a Chrome extension to trigger the web endpoint based on whatever text is highlighted. This would enable users to create issues from any logging service in their web browser and to select which type of Github issue template to file (currently, we only support 1 template). I attempted this, but ran into configuration issues and issues where the extension could not pick up the highlighted text. The code is currently excluded from this project.

I can also give users of the API the ability to change the temperature and preview the issue before filing it.

# Installation

setup python
====
install [python3](https://www.python.org/downloads/)

setup openai
====
1. [setup openai billing](https://platform.openai.com/account/billing/overview)
1. [view credits](https://platform.openai.com/account/usage)

Please view the [py](./py) folder for the README on how to run the Python server and the test script to create Github issues based on logs.
