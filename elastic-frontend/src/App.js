import SearchBar from './components/SearchBar';
import { Layout } from 'antd';
import CardBox from './components/Card';
import { useEffect } from 'react';
const { Header, Footer, Content } = Layout;

const App = () => {
  const data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
  useEffect(() => {}, []);
  
  return (
    <div>
      <secton className='navbar navbar-expand-lg bg-body-tertiary py-4 sticky-top mb-4'>
        <div className='container'>
          <SearchBar></SearchBar>
        </div>
      </secton>
      <div className='container'>
        <div className='flexc'>
          {data.map((ele, id) => (
            <CardBox key={id}></CardBox>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;
