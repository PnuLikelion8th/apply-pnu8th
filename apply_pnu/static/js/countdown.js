// ㅇㅇㅇ
const countDownClock = () => {
    const d = document;
    const daysElement = d.querySelector('.days');
    const hoursElement = d.querySelector('.hours');
    const minutesElement = d.querySelector('.minutes');
    const secondsElement = d.querySelector('.seconds');

    timer()


    function timer() {


        let countdown = setInterval(() => {
            const secondsLeft = Math.round((new Date(2020, 2, 23) - new Date()) / 1000);

            if (secondsLeft <= 0) {
                clearInterval(countdown);
                return;
            };

            displayTimeLeft(secondsLeft);

        }, 1000);
    }

    function displayTimeLeft(seconds) {
        daysElement.textContent = Math.floor(seconds / 86400);
        hoursElement.textContent = Math.floor((seconds % 86400) / 3600);
        minutesElement.textContent = Math.floor((seconds % 86400) % 3600 / 60);
        secondsElement.textContent = seconds % 60 < 10 ? `0${seconds % 60}` : seconds % 60;
    }
}


/*
  start countdown
  enter number and format
  days, hours, minutes or seconds
*/
// countDownClock(20, 'days');
countDownClock()