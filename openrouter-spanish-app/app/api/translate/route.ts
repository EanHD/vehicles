import { callOpenRouter } from "@/lib/openrouter";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const { phrase } = (await request.json()) as { phrase?: string };

  if (!phrase || !phrase.trim()) {
    return NextResponse.json(
      { error: "Please provide a phrase to translate." },
      { status: 400 }
    );
  }

  const translation = await callOpenRouter([
    {
      role: "system",
      content:
        "You are a Mexican Spanish translator. Translate the user phrase into natural Mexican Spanish. Return only the translation, no extra commentary."
    },
    {
      role: "user",
      content: phrase
    }
  ]);

  return NextResponse.json({ translation });
}
