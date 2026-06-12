import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6IKuJ8WR32_LrHbPIfDnP-w90Rv1vLWszIPBJCyewiNWA")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"✅ {m.name}")