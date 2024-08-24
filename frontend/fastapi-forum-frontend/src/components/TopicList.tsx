import React from "react";
import TopicListItem from "./TopicListItem";

interface TopicListProps {
  topics: any[]
}

const TopicList: React.FC<TopicListProps> = ({ topics }) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-2xl font-bold mb-4">话题列表</h2>
      <table className="table-auto w-full">
        <thead className="bg-gray-200">
          <tr>
            <th className="px-4 py-2">话题</th>
            <th className="px-4 py-2">回复</th>
            <th className="px-4 py-2">浏览量</th>
            <th className="px-4 py-2">活动</th>
          </tr>
        </thead>
        <tbody>
          {topics.map((topics)=>(
            <TopicListItem topic={topics} key={topics.title} />
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TopicList;


