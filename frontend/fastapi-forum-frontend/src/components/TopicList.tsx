import React from "react";
interface Topic {
  id: number;
  title: string;
  tags: string[];
}

const TopicList: React.FC = () => {
  // 假设这是一些模拟的主题数据
  const topics: Topic[] = [
    { id: 1, title: "Topic 1", tags: ["tag1", "tag2"] },
    { id: 2, title: "Topic 2", tags: ["tag3", "tag4"] },
    // 添加更多主题数据
  ];

  return (
    <div className="p-1">
      {topics.map((topic) => (
        <div key={topic.id} className="bg-white rounded p-4 mb-4 shadow">
          <h3 className="text-lg font-bold">{topic.title}</h3>
          <div className="flex flex-wrap">
            {topic.tags.map((tag) => (
              <span
                key={tag}
                className="bg-gray-200 rounded px-2 py-1 mr-2 mb-2"
              >
                {tag}
              </span>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default TopicList;
