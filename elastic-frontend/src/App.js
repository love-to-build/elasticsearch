import { useEffect, useState } from 'react';
import CardBox from './components/Card';
import SearchBar from './components/SearchBar';
const App = () => {
  const [data, setData] = useState([]);
  const [selectedOption, setSelectedOption] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [options, setOptions] = useState([]);
  let { lable } = selectedOption;

  lable = lable === 'undefined' ? '' : lable;

  useEffect(() => {
    search_req();
  }, [selectedOption]);

  const make_req = async () => {
    const response = await fetch(
      `http://localhost:8000/autocomplete?query=${inputValue}`
    );
    const data = await response.json();
    setOptions(data);
  };
  const search_req = async () => {
    const response = await fetch(
      `http://localhost:8000/string-query-search?query=${lable}`
    );

    const data = await response.json();
    console.log('searching data::::::::::::::::', data);
    setData(data);
  };
  // const options = [
  //   { label: 'hello', value: '1' },
  //   { label: 'codesandbox', value: '2' },
  //   { label: 'react', value: '3' },
  //   { label: 'nodejs', value: '4' },
  //   { label: 'java', value: '5' },
  //   { label: 'antd', value: '6' },
  //   { label: 'dependency', value: '7' },
  //   { label: 'less', value: '8' },
  // ];

  const onSelect = async (data, option) => {
    setSelectedOption(option);
    setInputValue(option.label);

    console.log('Selected option :::::::::::', lable);
  };

  const onChange = async (data, option) => {
    setInputValue(data);
    setSelectedOption(option);
    await make_req();
  };
  return (
    <div>
      <secton className='navbar navbar-expand-lg bg-body-tertiary py-4 sticky-top mb-4'>
        <div className='container'>
          <SearchBar
            inputValue={inputValue}
            options={options}
            onChange={onChange}
            onSelect={onSelect}
          ></SearchBar>
        </div>
      </secton>
      <div className='container'>
        <div className='flexc'>
          {data.map((ele, id) => (
            <CardBox ele={ele} key={id}></CardBox>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;
