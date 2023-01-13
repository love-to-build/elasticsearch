import React from 'react';
import { Card } from 'antd';
/**
 * 
 * @param {*} param0 
 * @returns
 * {
  "title": "Ra.One",
  "year": "2011",
  "certificate": "U",
  "duration": "156 min",
  "genre": "Action, Adventure, Sci-Fi            ",
  "desc": "Raj is a heartbreaker. His love stories with Mahi, Radhika, and Gayatri finally teach him about love and life in their own sweet, sexy, and sassy ways.",
  "rating": "6.2",
  "votes": "11,746"
}
 
 */
const CardBox = ({ ele }) => {
  const { title, year, certificate, duration, genre, desc, rating, votes } =
    ele;
  return (
    <Card className='card' title={title} style={{ width: 300 }}>
      <p>Description :{desc}</p>
      <p>Release Year: {year}</p>
      <p>Certificate :{certificate}</p>
      <p>Duration :{duration}</p>
      <p>Genre:{genre}</p>
      <p>Rating :{rating}</p>
      <p>Votes :{votes}</p>
    </Card>
  );
};

export default CardBox;
