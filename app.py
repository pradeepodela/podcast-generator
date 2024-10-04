# import streamlit as st
# from pydub import AudioSegment
# import google.generativeai as genai
# import json
# import uuid
# import io
# import edge_tts
# import asyncio
# import aiofiles
# import pypdf
# import os

# class PodcastGenerator:
#     def __init__(self):
#         pass

#     async def generate_script(self, prompt: str, language: str, api_key: str) -> dict:
#         # Example structure for the podcast script
#         example = """
#         {
#             "topic": "AGI",
#             "podcast": [
#                 {
#                     "speaker": 2,
#                     "line": "So, AGI, huh? Seems like everyone's talking about it these days."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Yeah, it's definitely having a moment, isn't it?"
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "It is and for good reason, right? I mean, you've been digging into this stuff, listening to the podcasts and everything. What really stood out to you? What got you hooked?"
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Honestly, it's the sheer scale of what AGI could do. We're talking about potentially reshaping well everything."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "No kidding, but let's be real. Sometimes it feels like every other headline is either hyping AGI up as this technological utopia or painting it as our inevitable robot overlords."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "It's easy to get lost in the noise, for sure."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "Exactly. So how about we try to cut through some of that, shall we?"
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Sounds like a plan."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "Okay, so first things first, AGI, what is it really? And I don't just mean some dictionary definition, we're talking about something way bigger than just a super smart computer, right?"
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Right, it's not just about more processing power or better algorithms, it's about a fundamental shift in how we think about intelligence itself."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "So like, instead of programming a machine for a specific task, we're talking about creating something that can learn and adapt like we do."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Exactly, think of it this way: Right now, we've got AI that can beat a grandmaster at chess but ask that same AI to, say, write a poem or compose a symphony. No chance."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "Okay, I see. So, AGI is about bridging that gap, creating something that can move between those different realms of knowledge seamlessly."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Precisely. It's about replicating that uniquely human ability to learn something new and apply that knowledge in completely different contexts and that's a tall order, let me tell you."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "I bet. I mean, think about how much we still don't even understand about our own brains."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "That's exactly it. We're essentially trying to reverse-engineer something we don't fully comprehend."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "And how are researchers even approaching that? What are some of the big ideas out there?"
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Well, there are a few different schools of thought. One is this idea of neuromorphic computing where they're literally trying to build computer chips that mimic the structure and function of the human brain."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "Wow, so like actually replicating the physical architecture of the brain. That's wild."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "It's pretty mind-blowing stuff and then you've got folks working on something called whole brain emulation."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "Okay, and what's that all about?"
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "The basic idea there is to create a complete digital copy of a human brain down to the last neuron and synapse and run it on a sufficiently powerful computer simulation."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "Hold on, a digital copy of an entire brain, that sounds like something straight out of science fiction."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "It does, doesn't it? But it gives you an idea of the kind of ambition we're talking about here and the truth is we're still a long way off from truly achieving AGI, no matter which approach you look at."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "That makes sense but it's still exciting to think about the possibilities, even if they're a ways off."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Absolutely and those possibilities are what really get people fired up about AGI, right? Yeah."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "For sure. In fact, I remember you mentioning something in that podcast about AGI's potential to revolutionize scientific research. Something about supercharging breakthroughs."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Oh, absolutely. Imagine an AI that doesn't just crunch numbers but actually understands scientific data the way a human researcher does. We're talking about potential breakthroughs in everything from medicine and healthcare to material science and climate change."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "It's like giving scientists this incredibly powerful new tool to tackle some of the biggest challenges we face."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Exactly, it could be a total game changer."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "Okay, but let's be real, every coin has two sides. What about the potential downsides of AGI? Because it can't all be sunshine and roses, right?"
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Right, there are definitely valid concerns. Probably the biggest one is the impact on the job market. As AGI gets more sophisticated, there's a real chance it could automate a lot of jobs that are currently done by humans."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "So we're not just talking about robots taking over factories but potentially things like, what, legal work, analysis, even creative fields?"
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Potentially, yes. And that raises a whole host of questions about what happens to those workers, how we retrain them, how we ensure that the benefits of AGI are shared equitably."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "Right, because it's not just about the technology itself, but how we choose to integrate it into society."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Absolutely. We need to be having these conversations now about ethics, about regulation, about how to make sure AGI is developed and deployed responsibly."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "So it's less about preventing some kind of sci-fi robot apocalypse and more about making sure we're steering this technology in the right direction from the get-go."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Exactly, AGI has the potential to be incredibly beneficial, but it's not going to magically solve all our problems. It's on us to make sure we're using it for good."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "It's like you said earlier, it's about shaping the future of intelligence."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "I like that. It really is."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "And honestly, that's a responsibility that extends beyond just the researchers and the policymakers."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "100%"
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "So to everyone listening out there I'll leave you with this. As AGI continues to develop, what role do you want to play in shaping its future?"
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "That's a question worth pondering."
#                 },
#                 {
#                     "speaker": 2,
#                     "line": "It certainly is and on that note, we'll wrap up this deep dive. Thanks for listening, everyone."
#                 },
#                 {
#                     "speaker": 1,
#                     "line": "Peace."
#                 }
#             ]
#         }
#                 """
#         language_instruction = (
#             f"- The podcast MUST be in {language} language" 
#             if language != "Auto Detect" 
#             else "- The podcast MUST be in the same language as the user input."
#         )

#         system_prompt = f"""
#         You are a professional podcast generator. Your task is to generate a professional podcast script based on the user input.
#         {language_instruction}
#         - The podcast should have 2 speakers.
#         - The podcast should be long and engaging.
#         - Follow this example structure:
#         {example}
#         """

#         user_prompt = f"Please generate a podcast script based on the following user input:\n{prompt}"

#         genai.configure(api_key=api_key)  # Use the provided API key

#         generation_config = {
#             "temperature": 1,
#             "max_output_tokens": 8192,
#             "response_mime_type": "application/json",
#         }

#         model = genai.GenerativeModel(
#             model_name="gemini-1.5-flash-002",
#             generation_config=generation_config
#         )

#         try:
#             response = await model.generate_content_async([{"role": "user", "parts": [user_prompt]}])
#             print(response.text)
#         except Exception as e:
#             st.error(f"Failed to generate podcast script: {e}")
#             return None
        
#         return json.loads(response.text)

#     async def tts_generate(self, text: str, speaker: int, speaker1: str, speaker2: str) -> str:
#         print(f"Generating audio for:")
#         voice = speaker1 if speaker == 1 else speaker2
#         speech = edge_tts.Communicate(text, voice)
#         temp_filename = f"temp_{uuid.uuid4()}.wav"
#         await speech.save(temp_filename)
#         print(f"Saved audio to: {temp_filename}")
#         return temp_filename

#     async def combine_audio_files(self, audio_files: list) -> str:
#         combined_audio = AudioSegment.empty()
#         for audio_file in audio_files:
#             combined_audio += AudioSegment.from_file(audio_file)
#             os.remove(audio_file)  # Remove individual files after combining
#         output_filename = f"output_{uuid.uuid4()}.wav"
#         combined_audio.export(output_filename, format="wav")
#         return output_filename

#     async def generate_podcast(self, input_text: str, language: str, speaker1: str, speaker2: str, api_key: str) -> str:
#         st.info("Generating podcast script...")
#         podcast_json = await self.generate_script(input_text, language, api_key)
#         if not podcast_json or 'podcast' not in podcast_json:
#             return None

#         st.info("Generating podcast audio files...")
#         audio_files = await asyncio.gather(
#             *[self.tts_generate(item['line'], item['speaker'], speaker1, speaker2) for item in podcast_json['podcast']]
#         )

#         combined_audio = await self.combine_audio_files(audio_files)
#         return combined_audio

# class TextExtractor:
#     @staticmethod
#     async def extract_from_pdf(file_path: str) -> str:
#         async with aiofiles.open(file_path, 'rb') as file:
#             content = await file.read()
#             pdf_reader = pypdf.PdfReader(io.BytesIO(content))
#             return "\n\n".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())

#     @staticmethod
#     async def extract_from_txt(file_path: str) -> str:
#         async with aiofiles.open(file_path, 'r') as file:
#             return await file.read()

#     @classmethod
#     async def extract_text(cls, file_path: str) -> str:
#         _, file_extension = os.path.splitext(file_path)
#         if file_extension.lower() == '.pdf':
#             return await cls.extract_from_pdf(file_path)
#         elif file_extension.lower() == '.txt':
#             return await cls.extract_from_txt(file_path)
#         else:
#             st.error(f"Unsupported file type: {file_extension}")
#             return None

# async def process_input(input_text: str, input_file, language: str, speaker1: str, speaker2: str, api_key: str = "") -> str:
#     st.info("Starting podcast generation...")

#     # Map the speaker names to their voice identifiers
#     voice_names = {
#         "Andrew - English (United States)": "en-US-AndrewMultilingualNeural",
#         "Ava - English (United States)": "en-US-AvaMultilingualNeural",
#         # Add more voices as needed
#     }

#     speaker1 = voice_names.get(speaker1, speaker1)
#     speaker2 = voice_names.get(speaker2, speaker2)

#     if input_file:
#         input_text = await TextExtractor.extract_text(input_file.name)

#     if not api_key:
#         st.error("Please provide a valid API key.")
#         return None

#     podcast_generator = PodcastGenerator()
#     podcast = await podcast_generator.generate_podcast(input_text, language, speaker1, speaker2, api_key)

#     return podcast

# # Streamlit Interface
# st.title("Podcast Generator")

# input_text = st.text_area("Input Text", placeholder="Enter text for podcast script")
# input_file = st.file_uploader("Or Upload a PDF/TXT file", type=["pdf", "txt"])
# language = st.selectbox("Select Language", ["Auto Detect", "English", "Spanish"])
# speaker1 = st.selectbox("Speaker 1 Voice", ["Andrew - English (United States)", "Ava - English (United States)"])
# speaker2 = st.selectbox("Speaker 2 Voice", ["Brian - English (United States)", "Emma - English (United States)"])
# api_key = st.text_input("Enter Gemini API Key")

# if st.button("Generate Podcast"):
#     if input_text or input_file:
#         podcast = asyncio.run(process_input(input_text, input_file, language, speaker1, speaker2, api_key))
#         if podcast:
#             st.audio(podcast)
#     else:
#         st.error("Please provide input text or upload a file.")



















import streamlit as st
from pydub import AudioSegment
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import json
import uuid
import io
import edge_tts
import asyncio
import aiofiles
import pypdf
import os
import time
from typing import List, Dict

class PodcastGenerator:
    def __init__(self):
        print("PodcastGenerator initialized.")

    async def generate_script(self, prompt: str, language: str, api_key: str) -> Dict:
        print(f"Generating podcast script with prompt: {prompt[:50]}... and language: {language}")

         
        # Example structure for the podcast script
        example = """
            {
    "topic": "Zoho Schools",
    "podcast": [
        {
            "speaker": 1,
            "line": "Okay, so like imagine this. What if there was a place where you didn't have to pay for college?"
        },
        {
            "speaker": 2,
            "line": "Hmm. Intriguing."
        },
        {
            "speaker": 1,
            "line": "And on top of that, they, like, actually paid you to go there. Paid you to go to college."
        },
        {
            "speaker": 2,
            "line": "Okay, now you've got my attention, right?"
        },
        {
            "speaker": 1,
            "line": "It sounds kind of crazy, but it gets even better. They guarantee you a job at a global tech company after you graduate."
        },
        {
            "speaker": 2,
            "line": "Wow. Hold on. Tuition free, paid stipend, guaranteed job. There's gotta be a catch."
        },
        {
            "speaker": 1,
            "line": "I know, that's exactly what we were thinking. It's like someone took every complaint about student debt and useless college courses and just, like, flipped the script."
        },
        {
            "speaker": 2,
            "line": "So where are we diving in today?"
        },
        {
            "speaker": 1,
            "line": "We're doing a deep dive into Zoho Schools."
        },
        {
            "speaker": 2,
            "line": "Zoho Schools?"
        },
        {
            "speaker": 1,
            "line": "Yeah, these schools created by Zoho, you know, the tech company. And they’re doing things completely differently."
        },
        {
            "speaker": 2,
            "line": "I'm familiar with Zoho, but this is the first I'm hearing about their schools."
        },
        {
            "speaker": 1,
            "line": "It's certainly a fascinating case study, right? It really challenges assumptions about the traditional education system, especially for, well, anyone really, but particularly for people looking to break into the tech world."
        },
        {
            "speaker": 2,
            "line": "So they've got their whole website, right. Like, it's wild. You go on there, and it's like, boom, alternate education universe."
        },
        {
            "speaker": 1,
            "line": "Okay, I'm pulling it up now. What am I looking for first thing?"
        },
        {
            "speaker": 2,
            "line": "Right. They don’t just have one Zoho School. They’ve got five different things within Zoho Schools."
        },
        {
            "speaker": 1,
            "line": "Five different schools?"
        },
        {
            "speaker": 2,
            "line": "Yeah. Technology, design, business, advanced studies, even graduate studies."
        },
        {
            "speaker": 1,
            "line": "Wow. So they’ve really got the full spectrum of education covered then."
        },
        {
            "speaker": 2,
            "line": "Yeah, that’s really interesting. It seems much more thought out than just a quick coding bootcamp or something."
        },
        {
            "speaker": 1,
            "line": "Right. And get this, it’s in India, too. But they take applications from anywhere in India. So they’re really looking to cultivate talent nationally."
        },
        {
            "speaker": 2,
            "line": "Yeah, like their own little tech talent incubator."
        },
        {
            "speaker": 1,
            "line": "That's a great way to put it. So they’re not just looking locally for people who already have some skills. They’re trying to find people with potential all over."
        },
        {
            "speaker": 2,
            "line": "Exactly. And the thing is, they’ve been doing this for a while."
        },
        {
            "speaker": 1,
            "line": "Oh yeah, 19 years, over 1600 graduates."
        },
        {
            "speaker": 2,
            "line": "That’s not like a new experiment."
        },
        {
            "speaker": 1,
            "line": "Yeah, that’s a pretty solid track record, right? Especially if you consider they make up 15% of Zoho’s workforce."
        },
        {
            "speaker": 2,
            "line": "Now that’s a serious commitment. It’s not just like, “Oh, look at us. We’re being charitable.”"
        },
        {
            "speaker": 1,
            "line": "Right. Exactly. They’re putting their money where their mouth is."
        },
        {
            "speaker": 2,
            "line": "It makes you wonder though, like, how do they actually measure if this is working long-term? You know, do these graduates stay with the company for years and years? Or if they leave, are they competitive in the job market?"
        },
        {
            "speaker": 1,
            "line": "Those are good questions. That would tell us a lot more, I think, than just the number of graduates."
        },
        {
            "speaker": 2,
            "line": "Totally. Because they’re so upfront about it. Even on their website, they have this whole thing with Zoho Schools. And they start off with, “How useful was college?”"
        },
        {
            "speaker": 1,
            "line": "Ooh, that’s a loaded question, isn’t it?"
        },
        {
            "speaker": 2,
            "line": "I know, right? It’s like they’re already challenging the whole system."
        },
        {
            "speaker": 1,
            "line": "Yeah, because who hasn’t asked themselves that at some point, right?"
        },
        {
            "speaker": 2,
            "line": "No, seriously. Especially when you’re, you know, maybe struggling to pay off loans or whatever."
        },
        {
            "speaker": 1,
            "line": "So they actually asked their employees, “How useful was college?”"
        },
        {
            "speaker": 2,
            "line": "Oh, really?"
        },
        {
            "speaker": 1,
            "line": "And most of them were like, “Nah, I learned what I actually use on the job.”"
        },
        {
            "speaker": 2,
            "line": "Interesting. See that? To me, that really highlights the disconnect between what traditional education is giving us and what employers actually need."
        },
        {
            "speaker": 1,
            "line": "Yeah, and it’s not just in tech. I mean, we see this everywhere. The skills gap is real."
        },
        {
            "speaker": 2,
            "line": "It’s like instead of all that theory, they’re like, “Nope, hands-on, let’s go.”"
        },
        {
            "speaker": 1,
            "line": "Practical experience from day one. Makes sense."
        },
        {
            "speaker": 2,
            "line": "And the curriculum is always changing, keeping up with all the latest stuff."
        },
        {
            "speaker": 1,
            "line": "And the teachers aren’t like professors who’ve never left a classroom. They’re pulling in actual professionals."
        },
        {
            "speaker": 2,
            "line": "Yeah, people from the industry. So they know what actually works, what you actually need."
        },
        {
            "speaker": 1,
            "line": "That’s a huge difference. I mean, I remember some of my professors—bless their hearts—but they hadn’t worked in the field for like decades."
        },
        {
            "speaker": 2,
            "line": "It’s like an apprenticeship but supercharged."
        },
        {
            "speaker": 1,
            "line": "Definitely. And honestly, that’s what employers are looking for now, right? Someone who can just jump in and get going."
        },
        {
            "speaker": 2,
            "line": "Totally. And it’s not even just the technical stuff, right? They’re teaching you how to think, how to solve problems."
        },
        {
            "speaker": 1,
            "line": "Right, how to communicate."
        },
        {
            "speaker": 2,
            "line": "Yeah, because that’s huge. Stuff you need anywhere, not just in a tech job."
        },
        {
            "speaker": 1,
            "line": "Absolutely. Being able to communicate your ideas clearly, work on a team, that’s valuable no matter what you do."
        },
        {
            "speaker": 2,
            "line": "Okay, so they had this whole section—\"What We Do Differently.”"
        },
        {
            "speaker": 1,
            "line": "Mhm."
        },
        {
            "speaker": 2,
            "line": "And it gets into the details. Like, they talk a lot about communication skills."
        },
        {
            "speaker": 1,
            "line": "Oh, interesting. What do they say?"
        },
        {
            "speaker": 2,
            "line": "Just that they want students to be able to clearly communicate ideas, which, I mean, duh. But it’s true. A lot of programs just skip over that part."
        },
        {
            "speaker": 1,
            "line": "Exactly. You could be the best coder, but if you can’t explain what you’re doing to the team, you’re stuck."
        },
        {
            "speaker": 2,
            "line": "Right. And they do have those testimonials, you know, from alumni."
        },
        {
            "speaker": 1,
            "line": "Right."
        },
        {
            "speaker": 2,
            "line": "And those are great, but we have to acknowledge it’s always going to be the success stories."
        },
        {
            "speaker": 1,
            "line": "Exactly. It’s important to find other perspectives too—maybe people who went through the program and didn’t love it, or haven’t had the same positive experience."
        },
        {
            "speaker": 2,
            "line": "So for everyone listening, really think about this—would you consider this at 18?"
        },
        {
            "speaker": 1,
            "line": "Yeah, because this isn’t just about one school in India, right? This gets at something bigger."
        },
        {
            "speaker": 2,
            "line": "Like what if this is the future of education?"
        },
        {
            "speaker": 1,
            "line": "Seriously. What if this is how we start to fix all those problems—student debt, skills not matching up with jobs?"
        },
        {
            "speaker": 2,
            "line": "Exactly. Imagine you graduate, you’re ready to work, and you don’t have those loans hanging over you. That’s life-changing."
        },
        {
            "speaker": 1,
            "line": "It’s like they found a way to make everyone happy—the students, the company—well, at least on the surface."
        },
        {
            "speaker": 2,
            "line": "Right. It’s a really interesting model, and it’s definitely worth keeping an eye on."
        },
        {
            "speaker": 1,
            "line": "But—and this is important—we can’t just ignore those potential downsides."
        },
        {
            "speaker": 2,
            "line": "Absolutely not. There are always trade-offs, and it’s about weighing those and figuring out what matters most to you."
        },
        {
            "speaker": 1,
            "line": "This whole thing with Zoho Schools, I think, is a good reminder that we can always rethink things."
        },
        {
            "speaker": 2,
            "line": "Totally. The system isn’t set in stone. We can challenge it, we can experiment, and we can find better ways to do things."
        },
        {
            "speaker": 1,
            "line": "So that wraps up our deep dive into Zoho Schools. It was fascinating to learn more about this."
        },
        {
            "speaker": 2,
            "line": "And for everyone listening, thanks for joining us. Don’t forget to check out our show notes for links and more info, and we’ll catch you next time."
        }
    ]
}

        
        """
                   

        if language == "Auto Detect":
            language_instruction = "- The podcast MUST be in the same language as the user input."
        else:
            language_instruction = f"- The podcast MUST be in {language} language"

        system_prompt = f"""
        
        You are a highly engaging highly convesational with real emotionas between speakers podcast generator. Your task is to generate a engaging podcast script based on the user input.
        {language_instruction}
        - The podcast should have 2 speakers.
        - The podcast should be long and engaging.
        - Follow this example structure:
        - It shouild be in emotional tone
        - IT shouild be as a realistic as engaging as possible
        - It should be as engaging as possible
        - It shouild not bore the listener
        - Add some humor and alos sarcasm to it to make it more engaging and interesting
        - Add some real life examples to make it more engaging
        - Never ever be boring
        - never ever be robotic
        - add emotions to it
        - make it as engaging as emotional cono bewtwen the speakers
        - make sure dont mke it look like a promotional podcast
        

        {example}
#         """
        user_prompt = f"Please generate a realistic conversational enaganing emotional podcast script based on the following user input:\n{prompt}"

        messages = [{"role": "user", "parts": [user_prompt]}]

        genai.configure(api_key=api_key)  # Use the provided API key

        generation_config = {
            "temperature": 1,
            "max_output_tokens": 8192,
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-002",
            generation_config=generation_config,
            safety_settings={
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE
            },
            system_instruction=system_prompt
        )

        try:
            print("Sending request to generate podcast script...")
            response = await model.generate_content_async(messages)
            print("Podcast script generated successfully.")
        except Exception as e:
            print(f"Error occurred while generating script: {e}")
            raise Exception(f"Failed to generate podcast script: {e}")
        open("podcast_script.json", "w").write(response.text)
        return json.loads(response.text)

    async def tts_generate(self, text: str, speaker: int, speaker1: str, speaker2: str) -> str:
        print(f"Generating TTS for speaker {speaker}: {text[:50]}...")
        voice = speaker1 if speaker == 1 else speaker2
        speech = edge_tts.Communicate(text, voice)

        temp_filename = f"temp_{uuid.uuid4()}.wav"
        try:
            await speech.save(temp_filename)
            print(f"TTS generated and saved as {temp_filename}")
            return temp_filename
        except Exception as e:
            print(f"Error during TTS generation: {e}")
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
            raise e

    async def combine_audio_files(self, audio_files: List[str]) -> str:
        print("Combining audio files...")
        combined_audio = AudioSegment.empty()
        for audio_file in audio_files:
            print(f"Adding {audio_file} to combined audio.")
            combined_audio += AudioSegment.from_file(audio_file)
            os.remove(audio_file)  # Clean up temporary files

        output_filename = f"output_{uuid.uuid4()}.wav"
        combined_audio.export(output_filename, format="wav")
        print(f"Combined audio saved as {output_filename}")
        return output_filename

    async def generate_podcast(self, input_text: str, language: str, speaker1: str, speaker2: str, api_key: str) -> str:
        print("Generating podcast...")
        start_time = time.time()
        podcast_json = await self.generate_script(input_text, language, api_key)
        print(f"Podcast script generated in {time.time() - start_time:.2f} seconds.")

        print("Generating podcast audio files...")
        start_time = time.time()
        audio_files = await asyncio.gather(
            *[self.tts_generate(item['line'], item['speaker'], speaker1, speaker2) for item in podcast_json['podcast']]
        )
        print(f"Podcast audio files generated in {time.time() - start_time:.2f} seconds.")

        combined_audio = await self.combine_audio_files(audio_files)
        return combined_audio

class TextExtractor:
    @staticmethod
    async def extract_from_pdf(file_path: str) -> str:
        print(f"Extracting text from PDF: {file_path}")
        async with aiofiles.open(file_path, 'rb') as file:
            content = await file.read()
            pdf_reader = pypdf.PdfReader(io.BytesIO(content))
            extracted_text = "\n\n".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
            print("Text extracted from PDF successfully.")
            return extracted_text

    @staticmethod
    async def extract_from_txt(file_path: str) -> str:
        print(f"Extracting text from TXT file: {file_path}")
        async with aiofiles.open(file_path, 'r') as file:
            extracted_text = await file.read()
            print("Text extracted from TXT successfully.")
            return extracted_text

    @classmethod
    async def extract_text(cls, file_path: str) -> str:
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == '.pdf':
            return await cls.extract_from_pdf(file_path)
        elif file_extension.lower() == '.txt':
            return await cls.extract_from_txt(file_path)
        else:
            raise Exception(f"Unsupported file type: {file_extension}")

async def process_input(input_text: str, input_file, language: str, speaker1: str, speaker2: str, api_key: str = "") -> str:
    print("Starting podcast generation process...")
    start_time = time.time()

    voice_names = {
        "Andrew - English (United States)": "en-US-AndrewMultilingualNeural",
        "Ava - English (United States)": "en-US-AvaMultilingualNeural",
        "Brian - English (United States)": "en-US-BrianMultilingualNeural",
        "Emma - English (United States)": "en-US-EmmaMultilingualNeural",
        "Florian - German (Germany)": "de-DE-FlorianMultilingualNeural",
        "Seraphina - German (Germany)": "de-DE-SeraphinaMultilingualNeural",
        "Remy - French (France)": "fr-FR-RemyMultilingualNeural",
        "Vivienne - French (France)": "fr-FR-VivienneMultilingualNeural"
    }

    speaker1 = voice_names[speaker1]
    speaker2 = voice_names[speaker2]

    if input_file:
        print("Extracting text from uploaded file...")
        input_text = await TextExtractor.extract_text(input_file.name)

    if not api_key:
        api_key = os.getenv("GENAI_API_KEY")

    podcast_generator = PodcastGenerator()
    podcast = await podcast_generator.generate_podcast(input_text, language, speaker1, speaker2, api_key)

    print(f"Podcast generated in {time.time() - start_time:.2f} seconds.")
    return podcast

# Define Streamlit interface
def main():
    st.title("Podcast Generator")
    input_text = st.text_area("Enter Input Text", "")
    language = st.selectbox("Select Language", ["Auto Detect", "English", "German", "French"])
    speaker1 = st.selectbox("Select Speaker 1 Voice", ["Andrew - English (United States)", "Ava - English (United States)"])
    speaker2 = st.selectbox("Select Speaker 2 Voice", ["Brian - English (United States)", "Emma - English (United States)"])
    api_key = st.text_input("Enter Google API Key", "")

    if st.button("Generate Podcast"):
        if not input_text and not input_file:
            st.error("Please enter text or upload a file.")
        else:
            st.write("Processing...")

            podcast = asyncio.run(process_input(input_text, input_file, language, speaker1, speaker2, api_key))
            st.audio(podcast, format="audio/wav")

if __name__ == "__main__":
    main()
