import TopicList from "@/components/TopicList";


interface Topic {
  title: string;
  replies: number;
  views: number;
  activity: string;
}

const Home: React.FC = () => {
  const topics: Topic[] = [
    { title: 'Windows上的UCRT的编译问题似乎解决了', replies: 41, views: 1400, activity: '3 分钟' },
    { title: 'doomemacs 如何禁用 evil', replies: 2, views: 43, activity: '12 分钟' },
    // 继续添加其他话题数据
  ];

  return (
    <div>
      <div className="flex-grow p-4">
        <TopicList topics={topics} />
      </div>
    </div>
  );
};

export default Home;

