👗 Smart Fashion AI Assistant

Language: Python

A console-based AI assistant that helps users coordinate outfits, makeup, and shoes for different occasions. The system suggests complementary items or evaluates compatibility based on color and style scoring.

⸻

💡 Project Overview

This project is a smart fashion assistant that:
	•	Suggests makeup and shoes based on the outfit.
	•	Suggests outfit and shoes based on makeup.
	•	Suggests outfit and makeup based on shoes.
	•	Checks overall compatibility when outfit, makeup, and shoes are provided together.
	•	Considers occasions like casual, party, and formal to adjust style recommendations.
	•	Calculates a compatibility score based on color coordination and style matching.

⸻

🛠 Features
	•	Dynamic suggestions based on partial inputs (outfit, makeup, or shoes).
	•	Compatibility scoring (0–100%) for full outfit, makeup, and shoe combinations.
	•	Verdict categories:
	•	Perfect match
	•	Good, minor improvements possible
	•	Needs improvement
	•	Handles different occasions: casual, party, and formal.

⸻

⚙️ How It Works
	1.	User selects an input option (outfit, makeup, shoes, or combination).
	2.	Inputs the items and occasion.
	3.	The system uses AI-inspired scoring functions:
	•	color_score() → Evaluates color coordination.
	•	style_score() → Evaluates style based on occasion.
	4.	Suggests missing items or calculates compatibility score.
	5.	Prints recommendations and compatibility verdict.

⸻

🏃 Usage
	1.	Run the Python script:
  python smart_fashion_ai.py
	2.	Follow the prompts to input your outfit, makeup, shoes, and occasion.
	3.	Receive recommendations or compatibility evaluation.

  
⸻

📌 Notes
	•	Input should be simple descriptive words, e.g., “black dress”, “bold makeup”, “heels”.
	•	Currently supports basic color and style matching.
	•	Can be extended to include more colors, makeup types, shoe styles, or even GUI integration.

⸻

⚡ Author

Shubhi Gupta – Developed as a Python-based AI assistant for fashion coordination and style compatibility.
