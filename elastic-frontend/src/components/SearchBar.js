import { UserOutlined } from '@ant-design/icons';
import { AutoComplete, Input } from 'antd';
import React from 'react';
const renderTitle = (title) => (
  <span>
    {title}
    <a
      style={{
        float: 'right',
      }}
      href='https://www.google.com/search?q=antd'
      target='_blank'
      rel='noopener noreferrer'
    >
      more
    </a>
  </span>
);
const renderItem = (title, count) => ({
  value: title,
  label: (
    <div
      style={{
        display: 'flex',
        justifyContent: 'space-between',
      }}
    >
      {title}
      <span>
        <UserOutlined /> {count}
      </span>
    </div>
  ),
});

const SearchBar = ({ inputValue, options, onSelect, onChange }) => {
  console.log('value and options ', inputValue, 'input value ', options);
  return (
    <AutoComplete
      value={inputValue}
      options={options}
      autoFocus={true}
      onSelect={onSelect}
      onChange={onChange}
      popupClassName='certain-category-search-dropdown'
      dropdownMatchSelectWidth={500}
      style={{
        width: 300,
      }}
    >
      <Input.Search size='large' placeholder='search here' />
    </AutoComplete>
  );
};
export default SearchBar;
