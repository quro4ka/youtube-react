import s from './InfoAboutUser.module.scss'

import UserInfoItem from "../UserInfoItem/UserInfoItem";

const InfoAboutUser = ()=>{
    const fieldsSettings = [
        {
            title: 'Логотип',
            description: 'Добавте лого в аккаунт'
        },
        {
            title:'Имя',
            description: 'ladick'
        },
        {
            title:'Дата рождения',
            description: '15.04.2002г.'
        },
        {
            title:'Пол',
            description: 'Мужской'
        },
        {
            title:'Электронная почта',
            description: 'polevskux@gmail.com'
        },
        {
            title:'Пароль',
            description: '**********'
        },
    ]

    return (

        <div className={s.wrapper__basicInformation}>
            <ul className={s.basicInformation}>
                <li className={s.item__info_title}>
                    <h4 className={s.info_title}>Информация о Вас</h4>
                </li>
                {
                    fieldsSettings.map((field,index)=>{
                        return(
                            <UserInfoItem key={index}
                                          title={field.title}
                                          description={field.description}
                            />
                        )
                    })

                }

            </ul>
        </div>


    )



}


export default InfoAboutUser