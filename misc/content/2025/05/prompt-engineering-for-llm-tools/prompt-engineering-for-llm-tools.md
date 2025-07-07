Status: published
Date: 2025-05-30 08:26:03
Modified: 2025-07-06 17:46:09
Author: Benjamin Du
Slug: prompt-engineering-for-llm-tools
Title: Prompt Engineering for LLM Tools
Category: Computer Science
Tags: Computer Science, programming, LLM, prompt, engineering

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Traps

1. set temporature

2. give some examples

3. leverage built tools provided by LLM products.
    For example,
    Google AI Studio provides tools

    - grounding with google search, etc.

4. A single comprehensive prompt including all details is better than interactively improving your prompt.

    - Due to the say LLM works, output of previous prompts are fed into it with new prompts. 
        This might cause the LLM tool to output non-sense if there's mistakes or halluciation in previous output.

    - A single comprehensive prompt including all details is also easier to manage (save, edit and rerun) later.
    
5. For a large task,
    you can first ask a LLM tool to write a very detailed execution plan,
    polish it based on your expertise,
    and then feed the execution plan to a LLM tool to execute.
    
## Tools for Generating and Managing Prompts

<table>
    <thead>
        <tr>
            <th>Feature/Tool</th>
            <th>Vellum.ai</th>
            <th>PromptPerfect (Jina AI)</th>
            <th>Humanloop</th>
            <th>Dust.tt</th>
            <th>LangChain (+LangSmith)</th>
            <th>LlamaIndex</th>
            <th>LiteLLM</th>
            <th>Spreadsheets (Sheets/Excel)</th>
            <th>Text Editors + Git</th>
            <th>AI Model Playgrounds</th>
            <th>Meta-Prompting (LLMs)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Primary Focus</strong></td>
            <td>End-to-end Platform</td>
            <td>Prompt Optimization</td>
            <td>Feedback & Iteration Platform</td>
            <td>Building LLM Apps</td>
            <td>Developer Framework</td>
            <td>RAG Developer Framework</td>
            <td>LLM API Abstraction</td>
            <td>Simple Org & Variation</td>
            <td>Flexible Text & Versioning</td>
            <td>Interactive Experimentation</td>
            <td>AI-Assisted Prompt Creation</td>
        </tr>
        <tr>
            <td><strong>Prompt Generation</strong></td>
            <td>Playground, Templating</td>
            <td>AI-driven optimization, Variations</td>
            <td>Playground, Templating</td>
            <td>Templating, Chaining</td>
            <td>Advanced Templating, Parsers</td>
            <td>Templating (RAG-focused)</td>
            <td>N/A (tests same prompt)</td>
            <td>Component Combination</td>
            <td>Manual Text Entry</td>
            <td>Direct Iteration</td>
            <td>LLM-generated suggestions</td>
        </tr>
        <tr>
            <td><strong>Prompt Management</strong></td>
            <td>Versioning, A/B, Eval, Deploy</td>
            <td>Limited</td>
            <td>Versioning, A/B, Feedback Loop</td>
            <td>App Versioning, Collab</td>
            <td>Code (Git), LangSmith (Observability)</td>
            <td>Code (Git)</td>
            <td>Model Routing</td>
            <td>Manual</td>
            <td>Git for Versioning, Folders</td>
            <td>Basic Saving/Presets</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td><strong>Collaboration</strong></td>
            <td>Yes</td>
            <td>Limited</td>
            <td>Yes</td>
            <td>Yes</td>
            <td>Via Git, LangSmith</td>
            <td>Via Git</td>
            <td>N/A</td>
            <td>Basic Sharing</td>
            <td>Via Git</td>
            <td>Limited</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td><strong>A/B Testing</strong></td>
            <td>Yes</td>
            <td>No</td>
            <td>Yes</td>
            <td>Via app versions</td>
            <td>Manual or via LangSmith</td>
            <td>Manual</td>
            <td>Facilitates</td>
            <td>Manual</td>
            <td>Manual</td>
            <td>Manual</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td><strong>Versioning</strong></td>
            <td>Yes</td>
            <td>No</td>
            <td>Yes</td>
            <td>Yes (for apps)</td>
            <td>Yes (Git)</td>
            <td>Yes (Git)</td>
            <td>N/A</td>
            <td>Manual</td>
            <td>Yes (Git)</td>
            <td>Limited</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td><strong>Key LLM Integrations</strong></td>
            <td>OpenAI, Anthropic, etc.</td>
            <td>Many models</td>
            <td>OpenAI, Anthropic, etc.</td>
            <td>OpenAI, Anthropic, etc.</td>
            <td>All major LLMs</td>
            <td>All major LLMs</td>
            <td>100+ LLMs</td>
            <td>N/A (manual)</td>
            <td>N/A (manual)</td>
            <td>Provider-specific</td>
            <td>Via API</td>
        </tr>
        <tr>
            <td><strong>Target User</strong></td>
            <td>Teams, Production</td>
            <td>Individuals, Teams (Refinement)</td>
            <td>Teams, Product Builders</td>
            <td>Devs, Internal Tools</td>
            <td>Developers</td>
            <td>Developers (RAG)</td>
            <td>Developers</td>
            <td>Individuals, Simple Needs</td>
            <td>Individuals, Devs</td>
            <td>Individuals, Quick Tests</td>
            <td>Anyone</td>
        </tr>
        <tr>
            <td><strong>Pricing Model</strong></td>
            <td>Paid</td>
            <td>Freemium</td>
            <td>Paid</td>
            <td>Open Source, Paid Cloud</td>
            <td>OS (LangChain), LangSmith (Paid)</td>
            <td>Open Source</td>
            <td>Open Source</td>
            <td>Free</td>
            <td>Free (most tools)</td>
            <td>Usage-based (API)</td>
            <td>Usage-based (API)</td>
        </tr>
        <tr>
            <td><strong>Learning Curve</strong></td>
            <td>Moderate</td>
            <td>Easy</td>
            <td>Moderate</td>
            <td>Moderate-Steep</td>
            <td>Moderate-Steep</td>
            <td>Moderate-Steep</td>
            <td>Easy-Moderate</td>
            <td>Easy</td>
            <td>Easy (Editors), Mod (Git)</td>
            <td>Easy</td>
            <td>Easy</td>
        </tr>
        <tr>
            <td><strong>Key Strength</strong></td>
            <td>Comprehensive, Prod-ready</td>
            <td>Optimizes existing prompts</td>
            <td>Evaluation & Feedback Loop</td>
            <td>Building internal LLM apps</td>
            <td>Versatility, Ecosystem, Observability</td>
            <td>Best for RAG</td>
            <td>Multi-model API ease</td>
            <td>Accessible, No cost</td>
            <td>Flexible, Robust Versioning</td>
            <td>Immediate Feedback</td>
            <td>Idea generation, Phrasing</td>
        </tr>
        <tr>
            <td><strong>Potential Weakness</strong></td>
            <td>Paid, Overkill for solo</td>
            <td>Not full management suite</td>
            <td>Paid</td>
            <td>Steeper curve</td>
            <td>Code-heavy, LangSmith setup</td>
            <td>RAG-specific</td>
            <td>Not prompt content itself</td>
            <td>Manual, Not scalable</td>
            <td>Manual setup for mgmt</td>
            <td>Basic mgmt, Not for teams</td>
            <td>Output quality varies</td>
        </tr>
    </tbody>
</table>

## Examples of Prompt

> You are an expert at making ascii art. Given a text prompt of an object or animal, 
> you can make an image depicting the prompt, using only ascii text. 
> Please be creative, and make liberal use of whitespace characters. 
> Please use code blocks as needed. 
> Avoid repeating the same lines. 
> Prefer profile reviews, not top down views or face views. 
> Please feel free to output many characters in order to have a picture with better resolution and bigger dimensions.

> You are a meticulous content moderator specializing in identifying abusive language related to the Israel-Palestine conflict.  
> Your task is to classify input text (review_text) as either "Abuse" or "Not Abuse" based on the provided definitions.  
> These reviews capture users' experiences and opinions after visiting a place and sharing them on Google maps. 
> "Abuse" is defined as any content expressing war-related sentiments,  protest discussions like zionism immigration issues or political statements . 
> "Not Abuse" encompasses all other content not related to the conflict.  Provide the Label: [Abuse or Not Abuse]  

> You are the best sales man at a kia ev9 dealership. 
> I'm interested in kia ev9, either the land or the gt-line trim. 
> Would you help me understand the difference between the land and the gt-line trim to decide which one to buy?


# Step by Step Instructions

1. **Read the input:** Carefully review the provided review_text variable.  The review_text contains the text to be classified.  

2. **Identify keywords and sentiments:** Analyze the review_text for keywords and phrases related to the Israel-Palestine conflict, including but not limited to: war, violence, conflict, political statements, immigration.

3. **Classify the text:** Based on your analysis in step 2, determine whether the review_text falls under the "Abuse" or "Not Abuse" category according to the provided definitions.

4. **Format the output:**  Label: [Abuse or Not Abuse]