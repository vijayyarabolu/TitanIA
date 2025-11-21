import React, { useState } from 'react';
import UploadSection from './components/UploadSection';
import AgentInterface from './components/AgentInterface';
import ResultsView from './components/ResultsView';

function App() {
  const [agentResult, setAgentResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 py-10 px-4 sm:px-6 lg:px-8">
      <div className="max-w-5xl mx-auto">
        <header className="mb-10 text-center">
          <h1 className="text-4xl font-extrabold text-gray-900 mb-2">TitanIA</h1>
          <p className="text-lg text-gray-600">Enterprise AI Reasoning Platform</p>
        </header>

        <main>
          <UploadSection />
          <AgentInterface onResult={setAgentResult} />

          {agentResult && (
            <div className="mt-8">
              <h2 className="text-2xl font-bold text-gray-900 mb-4">Analysis Results</h2>
              <ResultsView result={agentResult} />
            </div>
          )}
        </main>

        <footer className="mt-12 text-center text-gray-500 text-sm">
          &copy; {new Date().getFullYear()} TitanIA Platform. All rights reserved.
        </footer>
      </div>
    </div>
  );
}

export default App;
