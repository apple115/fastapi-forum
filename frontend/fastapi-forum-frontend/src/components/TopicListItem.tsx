import React from "react"


interface Topic {
  title: string;
  replies: number;
  views: number;
  activity: string;
}

interface TopicListItemProps {
  topic: Topic;
}

const TopicListItem:React.FC<TopicListItemProps> = ({topic}) => {
return (
    <tr className="hover:bg-gray-100">
      <td className="border px-4 py-2">{topic.title}</td>
      <td className="border px-4 py-2">{topic.replies}</td>
      <td className="border px-4 py-2">{topic.views}</td>
      <td className="border px-4 py-2">{topic.activity}</td>
    </tr>
  );
}


export default TopicListItem;

