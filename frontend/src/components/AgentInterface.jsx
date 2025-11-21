import React, { useState } from 'react';
import axios from 'axios';

const AgentInterface = ({ onResult }) => {
    const [query, setQuery] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!query.trim()) return;

        setLoading(true);
        try {
            const response = await axios.post('http://98.92.51.45:8000/api/v1/agents/run', { query });
            onResult(response.data);
        } catch (error) {
            console.error("Agent Error:", error);
            alert("Failed to run agent workflow");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="p-6 bg-white rounded-lg shadow-md mb-6">
            <h2 className="text-xl font-semibold mb-4 text-gray-800">Ask TitanIA</h2>
            <form onSubmit={handleSubmit} className="space-y-4">
                <textarea
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Enter your query here..."
                    className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent h-32"
                />
                <div className="flex justify-end">
                    <button
                        type="submit"
                        disabled={loading || !query.trim()}
                        className={`px-6 py-2 rounded-md text-white font-medium ${loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-indigo-600 hover:bg-indigo-700'
                            }`}
                    >
                        {loading ? 'Agents Working...' : 'Run Analysis'}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default AgentInterface;
