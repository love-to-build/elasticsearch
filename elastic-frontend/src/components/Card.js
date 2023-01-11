import React from 'react';
import { Card } from 'antd';
const CardBox = () => {
  return (
    <Card
      className='card'
      title='Default size card'
      extra={<a href='#'>More</a>}
      style={{ width: 300 }}
    >
      <p>Card content</p>
      <p>Card content</p>
      <p>Card content</p>
    </Card>
  );
};

export default CardBox;
