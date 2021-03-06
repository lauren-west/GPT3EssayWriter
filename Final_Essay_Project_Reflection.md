Lauren West and Evan Coulson
Prof. Dodds
CS181Y
6 May 2022
# Essay Generation 
## Project Reflection
### The Initial Vision and its Evolution
The initial vision for this project was to build an essay generator and make use of GPT-3. We wanted to work with the OpenAI API to have it generate essays and then have it grade itself. At the beginning of this project, we expected GPT-3 to generate an essay of the desired word length. As we worked on the OpenAI side of the project, we also decided that building a UI would be a universal way for people to interact with our project. Thus, we added Flask to our tech stack and built a backend that generated the essays with OpenAI and a frontend that allows users to input their prompts and view the essay in their web browser.

As we entered the presentation phase of the project, we began to solve the problems we encountered with OpenAI. We encountered three main problems with GPT-3. The first problem was that GPT-3 did not generate an entire essay when we prompted it with a word count and an essay prompt. We realized that we would not be able to control the word count, but we could at least generate an accurate number of paragraphs by designing an algorithm that had GPT-3 create an outline and then write a paragraph for each outline piece. The next problem we encountered was GPT-3 outputting random text sometimes; this is something that sometimes still appears in our essays and needs to be solved. The last problem that we encountered was that GPT-3 sometimes has grammatical errors and spelling mistakes, which we want to solve in the future.
### Progress and Final System's Capabilities
Our final system's capabilities include a website with a text area and a submission button that, on submit, generates an essay using GPT-3. Initially, the python backend was created, and this first consisted of a call to the OpenAI API that would give an essay less than 200 words long. The new iteration involved what we have named “the essay recipe,” consisting of distinct calls to the OpenAI’s API to create a thesis and an outline. Then, we made API calls to create intro, body, and conclusion paragraphs based on the outline guided by the thesis. This resulted in essays that approached a higher word count, cohesive ideas throughout the paper, and a (usually) satisfying conclusion.

The technologies used in this project include HTML, CSS, and Flask backend. The final product is pushed to this live site: ​​https://pacific-sea-61784.herokuapp.com/. The repository is located at https://github.com/lauren-west/GPT3EssayWriter. Another technology used is a conda environment that the README details how to generate and activate in two lines of code. Overall, the capabilities of the final system include a website that gets a user's input on an essay prompt, generates the essay, and displays it to the user.
### Extending the Project Further
There are two main extensions for this project that we foresee. To solve GPT-3’s grammatical and spelling mistakes, we want to integrate another API that can handle spelling mistakes and provide suggestions for correcting the essay before presenting it to the user. The second feature we want to add to our project is a plagiarism detector. We are curious if GPT-3 will ever plagiarise other essays on the internet or even repeat themselves between similar prompts. Adding in a plagiarism checker would allow us to provide feedback to the user about possible sources of plagiarism that GPT-3 might have used to generate the essay.
### What We Would Do Differently, In Retrospect
We would probably make very few changes if we had the opportunity to approach this project again since we had a very smooth experience developing our application. The main difficulties we encountered were with the UI design because we wrote the CSS/HTML/js from scratch and did not do it very cleanly. We could have used either a component library or CSS library to use ready-made components that are responsive to the viewport sizes; our app probably does not scale to mobile devices since it was designed for a desktop experience. 




