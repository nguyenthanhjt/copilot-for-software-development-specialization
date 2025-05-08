# Section 6: Hands-On Activity: Code Completion, Debugging, and Analysis With an LLM Chatbot

## Introduction

Welcome to the hands-on activity focused on utilizing Microsoft Copilot Chat for code completion, debugging, and analysis. This activity is designed to enhance your skills in using AI-driven tools for managing and improving code quality across various programming languages.

## Objectives

- Assess the capabilities of generative AI in assisting with coding applications.
- Assess the capabilities of generative AI in assisting with project management.
- Analyze the integration of generative AI into existing development workflows.

By the end of this activity, you will have practical experience in leveraging Copilot Chat for completing, debugging, and analyzing code, enhancing both your coding skills and your understanding of Copilot’s capabilities. 

In today’s fast-paced software development landscape, AI tools like Microsoft Copilot Chat have become essential. These tools assist developers not only in coding but also in project management, significantly enhancing productivity and efficiency.

## Importance of Using AI Tools in Coding and Project Management

AI-driven tools such as Microsoft Copilot can automate repetitive tasks, offer real-time code suggestions, and assist in debugging. This leads to higher-quality code and faster development cycles. For project management, AI tools streamline workflows, improve communication, and provide data-driven insights, making project oversight more efficient and effective. Integrating AI into your development process ensures that your team can maintain consistency, reduce errors, and focus on innovative solutions.

By embracing these tools, developers can stay ahead in a competitive field, ensuring that their projects are not only completed on time but also meet the highest quality standards.

## Instructions

Please download the following files before you start the hands-on activity.

Please refer the following code snippets before starting the hands-on activity

File 1: [calculate_factorial.py]

```py
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer: "))
        print(f"The factorial of {number} is {calculate_factorial(number)}")
    except ValueError as e:
        print(e)
```

File 2: [functions.js]

```js
function addNumbers(num1, num2) {
    return num1 + num2;
}

function calculateAverage(numbers) {
    const sum = numbers.reduce((acc, current) => acc + current, 0);
    return sum / numbers.length;
}
```

## Task 1: Code Completion in Python

**Objective**: Use Copilot Chat to complete a Python script by adding error handling and memoization, and creating a new route in a Flask application

1. Download the sample file:
   - Open your coding environment and activate Copilot.
   - Download the sample Python script (calculate_factorial.py) from the Course Resources section.
2. Prompt Copilot to translate the code:
   - In Copilot Chat, type: "I'm going to paste some Python code. Please analyze it and wait for further instructions."
   - Paste the code into the chat.
   - Next, type: "Complete the calculate_factorial function to include error handling and memoization. Then, add a new route '/factorial/int' that uses this function to return the factorial of the given number."
3. Review the generated code:
   - Copilot will provide a completed version of the calculate_factorial function and a new route.
   - Ensure the changes maintain the functionality of the factorial calculation.
   - Ensure the translated code maintains the functionality of calculating the Fibonacci sequence.
4. Understand the memoization concept:
   - In Copilot Chat, type: "Explain how the memoization in the calculate_factorial function works and why it's beneficial."
   - Review Copilot's explanation to understand the concept.
5. Enhance error-handling:
   - In Copilot Chat, type: "Enhance the '/factorial/int' route to handle very large numbers gracefully. If the result is too large to calculate, it should return an appropriate error message."
   - Implement the suggested changes in your code.

## Task 2: Debugging JavaScript Functions

**Objective**: Use Copilot Chat to debug and improve two JavaScript functions by fixing bugs and adding input validation.

1. Download the sample file:
   - Open your coding environment and activate Copilot Chat.
   - Download the sample JavaScript script (functions.js) from the Course Resources section.
2. Prompt Copilot to debug addNumbers function:
   - In Copilot Chat, type: "I'm going to paste some JavaScript code with bugs. Please analyze it and wait for further instructions."
   - Paste the code into the chat.
   - Next, type: "Debug the addNumbers function. It's supposed to add two numbers, but it's not working correctly when called with addNumbers(5)."
3. Review and implement the fix:
   - Copilot will identify the issue and suggest a fix.
   - Implement the suggested fix in your code.
4. Debug calculateAverage function:
   - In Copilot Chat, type: "The calculateAverage function works for non-empty arrays, but it doesn't handle empty arrays correctly. How can we fix this?"
   - Implement the suggested fix for handling empty arrays.

5. Understand JavaScript's division by zero:

   - In Copilot Chat, type: "Can you explain why dividing by zero in JavaScript doesn't throw an error, and what the result of such an operation is?"
   - Review Copilot's explanation to understand the behavior.

6. Add input validation:

   - In Copilot Chat, type: "Enhance both functions to check if the inputs are valid numbers. For addNumbers, both inputs should be numbers. For calculateAverage, all array elements should be numbers."
   - Implement the suggested changes in your code.

## Task 3: Project Management and Development Workflow Integration

**Objective**: Use Copilot Chat to assist with project management tasks and analyze how AI can integrate into existing development workflows.

1. Project task automation:

   - In Copilot Chat, type: "I'm working on a project management task. Can you help automate task assignments based on team members' skills and availability?"
   - Provide details about your project, including team members, their skills, and current availability.

2. Review and implement the suggested automation:

   - Copilot will provide a method or script to automate task assignments.
   - Review the suggested approach and implement it in your project management tool or workflow.

3. Workflow integration analysis:

   - In Copilot Chat, type: "Analyze our current development workflow and suggest improvements using AI tools."
   - Provide details about your current workflow, including stages like coding, testing, deployment, and maintenance.

4. Review workflow improvements:

   - Copilot will suggest improvements to integrate AI tools at various stages of your development workflow.
   - Review the suggestions and discuss with your team how to implement these improvements.

5. Enhance project management efficiency:

   - In Copilot Chat, type: "Suggest ways to improve our project management efficiency using AI."
   - Review Copilot's suggestions for improving project management efficiency, such as using AI for scheduling, resource allocation, and progress tracking. 

## Conclusion

By following these steps, you will have successfully utilized Microsoft Copilot Chat to complete, debug, and analyze code. You will have also learned how to use Microsoft Copilot Chat to improve project management tasks and integrate AI into your development workflows. This hands-on activity provides a structured approach to harnessing the power of AI-driven tools in your development process, enhancing both your coding skills and your understanding of Copilot’s capabilities.

If you encounter any challenges or need further assistance, refer to the provided additional resources or reach out for support.

Happy coding!

## Additional Reading

- GitHub Copilot Documentation
  - Official documentation for GitHub Copilot provides in-depth information on its features, setup, and usage.
  - [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- OpenAI Codex
  - Learn more about the underlying AI model powering GitHub Copilot and its capabilities.
  - [OpenAI Codex](https://openai.com/index/openai-codex/)
- Microsoft Copilot: A Guide to the AI Coding Assistant.
  - Learn more about Microsoft copilot and how to integrate it on various platforms and use it efficiently
  - [Medium](https://medium.com/@rmndrathna4/microsoft-copilot-a-guide-to-the-ai-coding-assistant-3e69c56e7917)

## References

- GitHub. (n.d.). GitHub Copilot: The world’s most widely adopted AI developer tool.  <https://github.com/features/copilot>
- Kerr, K. (2024, April 2). Using GitHub Copilot in your IDE: Tips, tricks, and best practices. GitHub Blog.  <https://github.blog/developer-skills/github/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/>
- Luca, J. (2023, November 1). Microsoft Copilot: A guide to the AI coding assistant.  <https://medium.com/@rmndrathna4/microsoft-copilot-a-guide-to-the-ai-coding-assistant-3e69c56e7917>
- Wojciech, Z., Brockman, G., & OpenAI. (2021, August 10). OpenAI Codex. OpenAI.  <https://openai.com/index/openai-codex/>
  
These resources will help you deepen your understanding of AI tools like GitHub Copilot and their applications in coding and project management. They provide a comprehensive overview of best practices, advanced features, and the latest developments in AI-driven software development.