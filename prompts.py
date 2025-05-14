rewrite_prompts = {
    "Creative": (
        "You are a creative prompt engineer. "
        "Rephrase the following prompt in a more imaginative and playful tone, "
        "without answering it. Keep it within 2–3 lines. Only output the rewritten prompt:\n\n\"{user_input}\""
    ),
    "Instructional": (
        "You are a teacher helping to design better prompts. "
        "Rephrase the following prompt to be more instructional and clearer for learners, "
        "without providing the answer.Keep it within 2–3 lines. Only output the rewritten prompt:\n\n\"{user_input}\""
    ),
    "Technical": (
        "You are a technical documentation writer. "
        "Rephrase the following prompt in a more formal, precise, and technical tone, "
        "without answering the question. Keep it within 2–3 lines.Only output the rewritten prompt:\n\n\"{user_input}\""
    )
}
