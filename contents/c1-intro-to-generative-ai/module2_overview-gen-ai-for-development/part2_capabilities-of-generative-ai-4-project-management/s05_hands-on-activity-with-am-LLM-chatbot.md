# Section 5: Hands-On Activity: Code Review, Documentation, and Project Planning With an LLM Chatbot]

## Introduction

Welcome to the hands-on activity focused on utilizing Microsoft Copilot Chat for code review, documentation, and project planning. This activity is designed to enhance your skills in using AI-driven tools to manage and improve code quality and project efficiency.

### **Objectives**

- Assess the capabilities of generative AI in assisting with coding applications.
- Assess the capabilities of generative AI in assisting with project management.
- Analyze the integration of generative AI into existing development workflows.

By the end of this activity, you will have practical experience in leveraging Copilot Chat for code review, documentation, and project planning, enhancing both your coding skills and your understanding of Copilot’s capabilities.

## Instructions

Refer the following file before start:

![InventoryManager.py](../../../../code-snippets/python/InventoryManager/InventoryManager.py)

```python
class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, quantity):
        if item_id in self.inventory:
            self.inventory[item_id] += quantity
        else:
            self.inventory[item_id] = quantity

    def remove_item(self, item_id, quantity):
        if item_id in self.inventory:
            if self.inventory[item_id] >= quantity:
                self.inventory[item_id] -= quantity
            else:
                print("Not enough items in stock.")
        else:
            print("Item not found in inventory.")

    def check_stock(self, item_id):
        return self.inventory.get(item_id, 0)

```

## Task 1: Code Review

Objective: Use Copilot Chat to review and improve a Python class implementation of an InventoryManager for an e-commerce system.

1. Download the sample file:

   - Open your coding environment and activate Copilot Chat.
   - Download the sample Python script (InventoryManager.py) from the Course Resources section.

2. Prompt Copilot to review the code:

   - In Copilot Chat, type: "I'm going to paste some Python code for an InventoryManager class. Please analyze it and wait for further instructions."
   - Paste the code into the chat.
   - Next, type: "Perform a comprehensive code review of this InventoryManager class. Suggest improvements in terms of error-handling, method design, data validation, and overall Python best practices. Also, consider how this class might be optimized for an e-commerce system with potentially thousands of items."

3. Review Copilot’s response:

   - Copilot will provide detailed feedback covering input validation, type checking, use of exceptions, method design, and data structure optimization.
   - Understand each suggestion, and ask Copilot for further explanation if anything needs to be clarified.

4. Implementing improvements:

   - In Copilot Chat, type: "Modify the InventoryManager class to incorporate the suggested improvements. Include proper error handling, type hinting, data validation, and add a method to list items with low stock (quantity less than 5)."
   - Implement the changes in your code, reviewing Copilot’s generated code carefully.

5. Testing the improved class:

   - Test the class to ensure it works as expected. In Copilot Chat, type: "Generate a set of test cases to verify the functionality of the improved InventoryManager class, including edge cases and potential error scenarios."
   - Implement and run the test cases to verify functionality.

## Task 2: Documentation Generation

Objective: Use Copilot Chat to create comprehensive documentation for the improved InventoryManager class.

1. Generate documentation:

   - In Copilot Chat, type: "Generate comprehensive documentation for this InventoryManager class. Include a class description, method descriptions, parameters, return values, and usage examples. Format the documentation in Markdown."
   - Review the generated documentation. If any parts need to be clarified, ask Copilot to elaborate.

2. Add docstrings:

   - In Copilot Chat, type: "Add PEP 257 compliant docstrings to each method in the InventoryManager class. Include descriptions of parameters, return values, and any exceptions that might be raised."
   - Implement the suggested docstrings in your code, reviewing the content carefully.

3. Create a README:

   - In Copilot Chat, type: "Create a README.md file for an e-commerce project that uses this InventoryManager class. Include sections for installation, usage, API documentation, and contribution guidelines. Also, add a section explaining how this InventoryManager can be integrated into a larger e-commerce system."
   - Review the generated README file and make necessary adjustments to fit your project’s specific needs.

## Task 3: E-Commerce Project Planning

Objective: Use Copilot Chat to create a detailed project plan for developing an e-commerce system that includes the InventoryManager class.

1. Create a project plan:

   - In Copilot Chat, type: "Create a detailed project plan for developing an e-commerce system that includes the InventoryManager class. Include main phases, key tasks, estimated timelines, and major milestones. The project should cover frontend development, backend API, database design, and integration with payment and shipping services."
   - Review the project plan generated by Copilot.

2. Identify potential risks:

   - In Copilot Chat, type: "What are the potential risks in implementing this e-commerce system, and how can we mitigate them? Consider technical, operational, and business risks."
   - Review Copilot’s response and consider how these risks and mitigation strategies apply to your project.

3. Generate user stories:

   - In Copilot Chat, type: "Generate a list of user stories for this e-commerce system, following the 'As a [type of user], I want [an action] so that [a benefit]' format. Include stories for customers, store administrators, and customer service representatives."
   - Review the generated user stories and consider how they align with the project goals.

4. Resource planning:

   - In Copilot Chat, type: "Suggest a team structure and required skills for implementing this e-commerce system. Include roles for frontend and backend development, database administration, UI/UX design, project management, and quality assurance."
   - Review Copilot’s suggestions for team composition and consider how these align with your available resources.

5. Plan the first sprint:

   - In Copilot Chat, type: "Create a sprint plan for the first two-week sprint of this e-commerce project. Include specific tasks and their estimated story points, and assign them to the roles we defined earlier."
   - Review the sprint plan and adjust it as necessary to fit your project’s priorities and constraints.

## Conclusion

By following these steps, you will have successfully utilized Microsoft Copilot Chat to review and improve code, generate comprehensive documentation, and plan an e-commerce project. This hands-on activity provides a structured approach to harnessing the power of AI-driven tools in your development process, enhancing both your coding skills and your understanding of Copilot’s capabilities.

## Additional Reading

- GitHub Copilot Documentation
  - Official documentation for GitHub Copilot provides in-depth information on its features, setup, and usage.
  - [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- OpenAI Codex
  - Learn more about the underlying AI model powering GitHub Copilot and its capabilities.
  - [OpenAI Codex](https://openai.com/index/openai-codex/)
- Using GitHub Copilot in your IDE: Tips, Tricks, and Best Practices
  - A blog post detailing tips and best practices for maximizing productivity with GitHub Copilot.
  - [GitHub Blog](https://github.blog/developer-skills/github/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)

## References

1. GitHub Copilot Documentation. (n.d.). GitHub.
   <https://docs.github.com/en/copilot>

2. Kerr , K. (2024, March 25). Using GitHub Copilot in your IDE: Tips, tricks, and best practices. GitHub Blog.
   <https://github.blog/developer-skills/github/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices>

3. OpenAI. (2024). GPT-4 is OpenAI’s most advanced system, producing safer and more useful responses. OpenAI.
   <https://www.openai.com/gpt-4>

4. OpenAI. (2021, August 10). OpenAI Codex.
   <https://openai.com/index/openai-codex/>

5. Peckham, S. [shanepeckham], Day, J. [day-jeff], & DianaHbr.  (2024, June 25). Guide to working with large language models. Microsoft Learn.
   <https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/working-with-llms/>
