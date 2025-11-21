import React from 'react';

const ResultsView = ({ result }) => {
    if (!result) return null;

    return (
        <div className="space-y-6">
            {/* Final Decision */}
            <div className="p-6 bg-white rounded-lg shadow-md border-l-4 border-green-500">
                <h2 className="text-xl font-semibold mb-2 text-gray-800">Final Decision</h2>
                <p className="text-gray-700 whitespace-pre-wrap">{result.decision}</p>
            </div>

            {/* Risk Analysis */}
            <div className="p-6 bg-white rounded-lg shadow-md border-l-4 border-yellow-500">
                <h2 className="text-xl font-semibold mb-2 text-gray-800">Risk Analysis</h2>
                <p className="text-gray-700 whitespace-pre-wrap">{result.risk_analysis}</p>
            </div>

            {/* Audit Log */}
            <div className="p-6 bg-gray-50 rounded-lg shadow-inner">
                <h2 className="text-lg font-semibold mb-3 text-gray-700">Audit Log</h2>
                <ul className="space-y-2">
                    {result.audit_log.map((log, index) => (
                        <li key={index} className="text-sm text-gray-600 font-mono border-b border-gray-200 pb-1 last:border-0">
                            {log}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default ResultsView;
