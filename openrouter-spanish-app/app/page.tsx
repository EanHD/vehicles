"use client";

import { useEffect, useMemo, useState } from "react";

type HistoryItem = {
  phrase: string;
  translation: string;
  createdAt: string;
};

const HISTORY_KEY = "mx-spanish-history";

export default function Home() {
  const [phrase, setPhrase] = useState("");
  const [goal, setGoal] = useState("");
  const [translation, setTranslation] = useState("");
  const [history, setHistory] = useState<HistoryItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [maestroLoading, setMaestroLoading] = useState(false);
  const [maestroContent, setMaestroContent] = useState("");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const stored = localStorage.getItem(HISTORY_KEY);
    if (stored) {
      try {
        const parsed = JSON.parse(stored) as HistoryItem[];
        setHistory(parsed);
      } catch (parseError) {
        console.error("Failed to parse history", parseError);
      }
    }
  }, []);

  useEffect(() => {
    localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
  }, [history]);

  const recentHistory = useMemo(() => history.slice(0, 12), [history]);

  async function handleTranslate() {
    setError(null);
    setLoading(true);
    setTranslation("");

    try {
      const response = await fetch("/api/translate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ phrase })
      });

      const data = (await response.json()) as {
        translation?: string;
        error?: string;
      };

      if (!response.ok) {
        throw new Error(data.error ?? "Translation failed.");
      }

      if (data.translation) {
        setTranslation(data.translation);
        const newItem: HistoryItem = {
          phrase,
          translation: data.translation,
          createdAt: new Date().toISOString()
        };
        setHistory((prev) => [newItem, ...prev]);
      }
    } catch (translateError) {
      setError(
        translateError instanceof Error
          ? translateError.message
          : "Translation failed."
      );
    } finally {
      setLoading(false);
    }
  }

  async function handleMaestro() {
    setError(null);
    setMaestroLoading(true);
    setMaestroContent("");

    try {
      const response = await fetch("/api/maestro", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ history, goal })
      });

      const data = (await response.json()) as { content?: string; error?: string };

      if (!response.ok) {
        throw new Error(data.error ?? "Maestro failed.");
      }

      setMaestroContent(data.content ?? "");
    } catch (maestroError) {
      setError(
        maestroError instanceof Error
          ? maestroError.message
          : "Maestro failed."
      );
    } finally {
      setMaestroLoading(false);
    }
  }

  function clearHistory() {
    setHistory([]);
    setTranslation("");
    setMaestroContent("");
    setPhrase("");
  }

  return (
    <main>
      <header>
        <span className="badge">OpenRouter · Maestro Mode</span>
        <h1>Maestro Español MX</h1>
        <p>
          Drop in an English phrase, get Mexican Spanish back, and let Maestro
          craft practice materials based on what you want to say.
        </p>
      </header>

      <section>
        <div className="grid two">
          <div className="stack">
            <label htmlFor="phrase">English phrase</label>
            <textarea
              id="phrase"
              rows={4}
              placeholder="Example: I want to schedule a brake inspection."
              value={phrase}
              onChange={(event) => setPhrase(event.target.value)}
            />
            <div className="actions">
              <button
                type="button"
                onClick={handleTranslate}
                disabled={loading || !phrase.trim()}
              >
                {loading ? "Translating..." : "Translate to MX Spanish"}
              </button>
              <button type="button" onClick={clearHistory}>
                Clear session
              </button>
            </div>
            {error ? <p className="notice">{error}</p> : null}
          </div>

          <div className="stack">
            <label htmlFor="translation">Translation</label>
            <textarea
              id="translation"
              rows={4}
              placeholder="Your translation will appear here."
              value={translation}
              readOnly
            />
            <p className="notice">
              History is stored locally in your browser. Connect a database
              later for multi-device tracking.
            </p>
          </div>
        </div>
      </section>

      <section>
        <div className="stack">
          <label htmlFor="goal">Learner goal (optional)</label>
          <input
            id="goal"
            type="text"
            placeholder="Example: Customer service, travel, medical visits"
            value={goal}
            onChange={(event) => setGoal(event.target.value)}
          />
          <button
            type="button"
            onClick={handleMaestro}
            disabled={maestroLoading || history.length === 0}
          >
            {maestroLoading ? "Generating..." : "Generate Maestro Practice"}
          </button>
        </div>
      </section>

      <section className="grid two">
        <div className="stack">
          <h2>Maestro output</h2>
          {maestroContent ? (
            <pre>{maestroContent}</pre>
          ) : (
            <p className="notice">
              Generate practice after you have at least one translation.
            </p>
          )}
        </div>
        <div className="stack">
          <h2>Recent phrases</h2>
          {recentHistory.length === 0 ? (
            <p className="notice">No translations yet.</p>
          ) : (
            <ul className="history-list">
              {recentHistory.map((item) => (
                <li key={item.createdAt} className="history-item">
                  <strong>{item.phrase}</strong>
                  <span>{item.translation}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      </section>
    </main>
  );
}
