import google.generativeai as genai
import subprocess
import os
import sys

API_KEY = "" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash') 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "TURKI-20260410-174125.dmp")
VOL_PATH = os.path.join(BASE_DIR, "volatility3", "vol.py")

def get_brief_analysis():
    print("[*] Shadow is starting brief investigation...")
    
    cmd = [sys.executable, VOL_PATH, "-f", MEMORY_FILE, "windows.pslist"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        short_data = result.stdout[:2000] 
        
        if not short_data:
            return "No data found."

        print("[*] Sending summary to AI Shadow...")
        prompt = f"Analyze these Windows processes for anything suspicious. Keep it brief. \n {short_data}"
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    report = get_brief_analysis()
    print("\n" + "="*30)
    print("   SHADOW BRIEF REPORT")
    print("="*30 + "\n")
    print(report)
