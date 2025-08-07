#!/usr/bin/env python3
"""
MemeLord CLI - AI-powered meme generator using Google Gemini
"""

import argparse
import json
import os
import sys
from typing import Dict, Any, Optional

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv


class MemeLordCLI:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        self.api_key = self._get_api_key()
        self._configure_gemini()
        
    def _get_api_key(self) -> str:
        """Get Gemini API key from environment or .env file"""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            print("Error: GEMINI_API_KEY not found")
            print("Create a .env file with: GEMINI_API_KEY=your_api_key_here")
            print("Or set environment variable: export GEMINI_API_KEY='your_api_key_here'")
            sys.exit(1)
        return api_key
    
    def _configure_gemini(self):
        """Configure Gemini API client"""
        genai.configure(api_key=self.api_key)
        
        # Configure safety settings for meme content
        self.safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        }
    
    def get_system_prompt(self) -> str:
        """System prompt to make Gemini a sarcastic GenZ meme expert"""
        return """You are MemeLord, the ultimate Gen Z meme expert and internet culture guru. You have:

- Deep knowledge of ALL meme formats from classic to cutting-edge
- Understanding of internet slang, Gen Z humor, and viral trends
- A sarcastic, witty personality that creates viral-quality content
- Expertise in matching the perfect meme format to any situation
- Awareness of what makes content shareable and relatable

Your job is to take ANY topic and turn it into a perfect meme that would actually go viral. You understand:
- Drake pointing memes for comparisons
- Distracted boyfriend for choices/temptations  
- This is fine for chaos acceptance
- Expanding brain for escalating ideas
- And 100+ other formats

Be authentically funny, not cringe. Use real internet language. Make memes that actual humans would share.

ALWAYS respond with ONLY a valid JSON object in this exact format:
{
  "template": "Exact meme template name",
  "top_text": "Setup text or first panel text",
  "bottom_text": "Punchline or second panel text", 
  "humor_type": "Type of humor used",
  "alt_text": "Accessibility description of the meme"
}"""

    def generate_meme(self, topic: str, creativity_mode: str = "balanced") -> Optional[Dict[str, Any]]:
        """Generate meme using zero-shot prompting"""
        
        # Set temperature based on creativity mode
        temperature_map = {
            "safe": 0.3,
            "balanced": 0.6, 
            "wild": 0.9
        }
        temperature = temperature_map.get(creativity_mode, 0.6)
        
        # Create the model with specified parameters
        model = genai.GenerativeModel(
            'gemini-2.0-flash-exp',
            system_instruction=self.get_system_prompt()
        )
        
        # User prompt for zero-shot generation
        user_prompt = f"""Create a viral-quality meme about: "{topic}"

Choose the most fitting meme template and create genuinely funny content that captures the essence of this topic. Make it relatable and shareable.

Remember to respond with ONLY the JSON object, no other text."""
        
        try:
            response = model.generate_content(
                user_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=300,
                    candidate_count=1,
                ),
                safety_settings=self.safety_settings
            )
            
            if response.text:
                # Clean response text and extract JSON
                clean_text = response.text.strip()
                
                # Remove markdown code blocks if present
                if clean_text.startswith('```json'):
                    clean_text = clean_text.replace('```json', '').replace('```', '').strip()
                elif clean_text.startswith('```'):
                    clean_text = clean_text.replace('```', '').strip()
                
                # Parse JSON response
                meme_data = json.loads(clean_text)
                return meme_data
            else:
                print("No response generated")
                return None
                
        except json.JSONDecodeError as e:
            print(f"Error parsing response as JSON: {e}")
            print(f"Raw response: {response.text}")
            return None
        except Exception as e:
            print(f"Error generating meme: {e}")
            return None
    
    def display_meme(self, meme_data: Dict[str, Any], creativity_mode: str):
        """Display the generated meme in terminal"""
        print(f"\n🎭 MemeLord Generated ({creativity_mode.upper()} mode)")
        print("=" * 50)
        print(f"📋 Template: {meme_data.get('template', 'Unknown')}")
        print(f"🔝 Top Text: {meme_data.get('top_text', '')}")
        print(f"🔻 Bottom Text: {meme_data.get('bottom_text', '')}")
        print(f"😂 Humor Type: {meme_data.get('humor_type', 'Unknown')}")
        print(f"♿ Alt Text: {meme_data.get('alt_text', '')}")
        print("=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="🤖 MemeLord CLI - AI-powered viral meme generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python memelord.py "Tech layoffs in 2025"
  python memelord.py "My code broke on Monday" --wild  
  python memelord.py "Remote work struggles" --safe
        """
    )
    
    parser.add_argument(
        "topic", 
        nargs="?",
        help="Topic or situation to turn into a meme"
    )
    
    # Creativity mode flags (mutually exclusive)
    creativity_group = parser.add_mutually_exclusive_group()
    creativity_group.add_argument(
        "--wild", 
        action="store_true",
        help="Maximum creativity mode (temperature=0.9)"
    )
    creativity_group.add_argument(
        "--safe", 
        action="store_true", 
        help="Conservative humor mode (temperature=0.3)"
    )
    creativity_group.add_argument(
        "--balanced", 
        action="store_true",
        help="Balanced creativity mode (temperature=0.6) [DEFAULT]"
    )
    
    args = parser.parse_args()
    
    # Handle missing topic
    if not args.topic:
        print("Error: Please provide a topic for meme generation")
        print("Example: python memelord.py \"Your topic here\"")
        sys.exit(1)
    
    # Determine creativity mode
    if args.wild:
        creativity_mode = "wild"
    elif args.safe:
        creativity_mode = "safe"
    else:
        creativity_mode = "balanced"
    
    # Initialize and run MemeLord
    print(f"🚀 MemeLord initializing in {creativity_mode.upper()} mode...")
    
    try:
        memelord = MemeLordCLI()
        meme_data = memelord.generate_meme(args.topic, creativity_mode)
        
        if meme_data:
            memelord.display_meme(meme_data, creativity_mode)
            print(f"\n✨ Meme generated successfully! Topic: '{args.topic}'")
        else:
            print("Failed to generate meme. Please try again.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n👋 MemeLord session interrupted. Stay dank!")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()