import React from "react";
import TopicListItem from "./TopicListItem";

interface TopicListProps {
  topics: any[];
}

const TopicList: React.FC<TopicListProps> = ({ topics }) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-2xl font-bold mb-4">话题列表</h2>
      {topics.map((topic) => (
        <div
          key={topic.title}
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: "12px",
            borderBottom: "1px solid #f0f0f0",
          }}
        >
          <div style={{ flex: 1 }}>
            <p>{topic.title}</p>
          </div>
          <div style={{ flex: 1, textAlign: "center" }}>
            <p>{topic.replies}</p>
          </div>
          <div style={{ flex: 1, textAlign: "center" }}>
            <p>{topic.views}</p>
          </div>
          <div style={{ flex: 1, textAlign: "center" }}>
            <p>活动内容（待完善）</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default TopicList;
