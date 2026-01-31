ServerEvents.tick(event => {
    // Получаем сервер и мир (Overworld)
    let server = event.server
    let level = server.getLevel('minecraft:overworld')

    // Если мира нет (напр. при старте), выходим
    if (!level) return

    // 1. Отключаем ванильный цикл смены дня и ночи
    // Это нужно, чтобы мы могли сами крутить время с нужной скоростью
    if (level.getGameRules().getBoolean('doDaylightCycle')) {
        level.getGameRules().get('doDaylightCycle').set(false, server)
        console.log("Vanilla Daylight Cycle Disabled by time_control.js")
    }

    // 2. Настройки скорости (Множители)
    // < 1.0 = Время идет медленнее (День длиннее)
    // > 1.0 = Время идет быстрее (Ночь короче)

    let daySpeed = 0.5   // 0.5 = День длится в 2 раза дольше (40 минут вместо 20)
    let nightSpeed = 2.0 // 2.0 = Ночь проходит в 2 раза быстрее (3.5 минуты вместо 7)

    // 3. Получаем текущее время
    // 0 - 24000 (один цикл), но getDayTime возвращает полное время (напр. 150000)
    let currentTime = level.getDayTime()
    let timeOfDay = currentTime % 24000

    // Ночь примерно с 13000 до 23000 (или до 0/24000)
    // isDay: 23500 - 12500 ? Упростим: 0-12000 это утро/день, 12000-24000 вечер/ночь
    // Точнее: спать можно с 12542. Солнце садится.

    let isNight = (timeOfDay >= 13000 && timeOfDay <= 23000)

    // Выбираем скорость
    let speed = isNight ? nightSpeed : daySpeed

    // 4. Логика накопления времени
    // Так как мы не можем добавить "0.5 тика", мы копим дробную часто
    let pData = server.persistentData
    if (!pData.timeAccumulator) pData.timeAccumulator = 0.0

    pData.timeAccumulator += speed

    // Если накопился целый тик (или больше)
    if (pData.timeAccumulator >= 1.0) {
        let ticksToAdd = Math.floor(pData.timeAccumulator)

        // Двигаем время вперед
        level.setDayTime(currentTime + ticksToAdd)

        // Убираем то, что добавили, из "копилки"
        pData.timeAccumulator -= ticksToAdd
    }
})

// На случай, если нужно спать
// Ванильный сон сбрасывает время, но при doDaylightCycle=false он может вести себя странно.
// Обычно Minecraft сам обрабатывает сон и ставит время на утро, даже если цикл выключен.
// Но если будут проблемы, можно добавить обработчик SleepEvent.
