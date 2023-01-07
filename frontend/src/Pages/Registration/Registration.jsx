import { RegistrationForm } from '../../components/RegistrationForm/RegistrationForm'
import s from './Registration.module.scss'

export const Registration = () => {
  return (
    <div className="main_registration">
      <div className={s.registration}>
        <div className={s.container}>
          <div className={s.wrapper}>
            <div className={s.header}>
              <div className={s.logo}>
                <svg viewBox="0 0 32 32" width="30px" height="30px">
                  <path
                    d="M 16 3 C 12.90625 3 10.507813 7.578125 10.078125 13.9375 C 10.632813 14.527344 11.285156 15.113281 12.007813 15.683594 C 12.015625 15.019531 12.054688 14.386719 12.109375 13.765625 C 12.691406 13.363281 13.421875 12.871094 14 12.535156 C 16.660156 11 19.398438 9.988281 21.707031 9.6875 C 22.160156 9.628906 22.585938 9.601563 22.972656 9.601563 C 24.269531 9.601563 25.1875 9.914063 25.527344 10.5 C 25.832031 11.03125 25.695313 11.875 25.183594 12.863281 C 25.707031 13.347656 26.203125 13.839844 26.644531 14.335938 C 27.769531 12.472656 28 10.78125 27.257813 9.5 C 26.375 7.972656 24.316406 7.332031 21.453125 7.703125 C 18.886719 8.035156 15.886719 9.136719 13 10.804688 C 12.816406 10.910156 12.644531 11.027344 12.464844 11.140625 C 13.183594 7.441406 14.644531 5 16 5 C 16.632813 5 17.289063 5.539063 17.882813 6.476563 C 18.5625 6.265625 19.234375 6.082031 19.886719 5.945313 C 18.851563 4.089844 17.507813 3 16 3 Z M 9.21875 7.613281 C 7.050781 7.574219 5.480469 8.222656 4.742188 9.5 C 3.9375 10.890625 4.273438 12.757813 5.65625 14.808594 C 5.78125 15 5.917969 15.203125 6.089844 15.425781 C 7.660156 17.480469 10.113281 19.527344 13 21.195313 C 13.183594 21.300781 13.375 21.394531 13.5625 21.5 C 12.417969 21.894531 11.308594 22.179688 10.289063 22.3125 C 8.339844 22.566406 6.914063 22.261719 6.476563 21.5 C 6.167969 20.96875 6.304688 20.125 6.816406 19.136719 C 6.292969 18.652344 5.796875 18.160156 5.351563 17.667969 C 4.230469 19.527344 4 21.21875 4.742188 22.5 C 5.460938 23.746094 6.960938 24.402344 9.039063 24.402344 C 9.511719 24.402344 10.019531 24.367188 10.546875 24.296875 C 10.851563 24.257813 11.15625 24.207031 11.46875 24.144531 L 11.6875 24.097656 C 11.703125 24.097656 11.714844 24.09375 11.730469 24.089844 C 12.261719 23.976563 12.847656 23.820313 13.519531 23.609375 L 14.179688 23.40625 C 15.160156 23.070313 16.164063 22.652344 17.167969 22.164063 C 17.386719 21.4375 17.582031 20.589844 17.730469 19.613281 C 17.152344 19.9375 16.570313 20.230469 15.992188 20.503906 C 15.324219 20.191406 14.652344 19.84375 14 19.464844 C 11.335938 17.925781 9.089844 16.0625 7.679688 14.214844 C 6.484375 12.648438 6.035156 11.261719 6.476563 10.5 C 6.777344 9.976563 7.574219 9.679688 8.671875 9.625 C 8.828125 8.917969 9.007813 8.246094 9.21875 7.613281 Z M 20.742188 11.898438 C 19.953125 12.082031 19.117188 12.351563 18.261719 12.691406 C 18.828125 13.027344 19.367188 13.386719 19.890625 13.746094 C 19.953125 14.472656 20 15.214844 20 16 C 20 21.898438 18.144531 26.398438 16.359375 26.941406 C 16.238281 26.980469 16.113281 27 16 27 C 15.367188 27 14.710938 26.464844 14.117188 25.519531 C 13.4375 25.734375 12.765625 25.917969 12.113281 26.054688 C 13.148438 27.910156 14.492188 29 16 29 C 16.199219 29 16.390625 28.980469 16.578125 28.941406 C 19.707031 28.347656 22 22.988281 22 16 C 22 15.785156 21.984375 15.578125 21.980469 15.363281 C 22.894531 16.15625 23.699219 16.972656 24.324219 17.785156 C 25.515625 19.351563 25.964844 20.738281 25.527344 21.5 C 25.21875 22.027344 24.433594 22.332031 23.328125 22.386719 C 23.171875 23.085938 22.996094 23.761719 22.785156 24.390625 C 22.839844 24.390625 22.90625 24.402344 22.960938 24.402344 C 25.039063 24.402344 26.539063 23.746094 27.257813 22.5 C 28.140625 20.972656 27.664063 18.867188 25.910156 16.574219 C 24.667969 14.949219 22.867188 13.332031 20.742188 11.898438 Z M 16 14 C 14.894531 14 14 14.894531 14 16 C 14 17.105469 14.894531 18 16 18 C 17.105469 18 18 17.105469 18 16 C 18 14.894531 17.105469 14 16 14 Z"/>
                </svg>
                <span>Losti</span>
              </div>

              <h1 className={s.main_title}>Создайте аккаунт</h1>
              {/*<h2 className={s.second_title}>Перейдите на YouTube</h2>*/}
            </div>

            <div className={s.users_block}>
              <RegistrationForm />
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
