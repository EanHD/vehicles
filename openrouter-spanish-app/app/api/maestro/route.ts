import { callOpenRouter } from "@/lib/openrouter";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const { history, goal } = (await request.json()) as {
    history?: { phrase: string; translation: string }[];
    goal?: string;
  };

  if (!history || history.length === 0) {
    return NextResponse.json(
      { error: "Add at least one translation to generate practice." },
      { status: 400 }
    );
  }

  const promptLines = history
    .map((item, index) => `${index + 1}. ${item.phrase} → ${item.translation}`)
    .join("\n");

  const content = await callOpenRouter([
    {
      role: "system",
      content:
        "You are Maestro, a Spanish study coach. Create practice material for Mexican Spanish learners. Produce a concise study guide, a 5-question quiz, and a short roleplay practice based on the phrases provided. Use bullet points and clear section headings."
    },
    {
      role: "user",
      content: `Here are the recent translations:\n${promptLines}\n\nLearner goal: ${
        goal ?? "Everyday conversational Mexican Spanish"
      }\n\nGenerate the study guide, quiz, and roleplay practice.`
    }
  ]);

  return NextResponse.json({ content });
}
