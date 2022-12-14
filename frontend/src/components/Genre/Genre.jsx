import { useSelector } from 'react-redux'
import s from './Genre.module.scss'

import cn from 'classnames'

let classNames = cn(s.genres__item, s.genres__active)

export const Genre = ({ genre, genreId, onClickGenre }) => {
  const genreIsChecked = useSelector((state) => state.genres.genreIsChecked)

  return (
    <li
      onClick={onClickGenre}
      className={`${genreId === genreIsChecked ? classNames : s.genres__item}`}>
      <a href="#" className={s.genres__link}>
        {genre.title}
      </a>
    </li>
  )
}
