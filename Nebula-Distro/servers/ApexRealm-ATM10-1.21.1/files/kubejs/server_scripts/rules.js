ServerEvents.commandRegistry(event => {
    const { commands: Commands, arguments: Arguments } = event

    event.register(
        Commands.literal('rules')
            .executes(c => {
                let player = c.source.player
                if (!player) return 0

                // Заголовок
                player.tell(Component.yellow('=== 📜 Правила Сервера ApexRealm 📜 ==='))
                player.tell(Component.string('')) // Пустая строка

                // Список правил
                let rules = [
                    "1. §cНикакого гриферства!§r (Используйте приваты FTB Chunks)",
                    "2. §9Уважайте других игроков.§r Без оскорблений и спама.",
                    "3. §eЧиты и эксплойты запрещены.§r (X-Ray, killaura и т.д.)",
                    "4. §aPvP только по согласию.§r Не убивайте новичков.",
                    "5. §dНе ломайте экономику.§r (Дюпы = бан)",
                    "6. §6Веселитесь!§r Это самое главное правило."
                ]

                rules.forEach(rule => {
                    player.tell(Component.of(rule))
                })

                player.tell(Component.string(''))
                player.tell(Component.gray('Используйте /discord для связи с админами.'))

                return 1
            })
    )

    // Доп. команда для ссылки на дискорд (часто просят вместе с правилами)
    event.register(
        Commands.literal('discord')
            .executes(c => {
                let player = c.source.player
                if (!player) return 0
                player.tell(Component.blue('Наш Discord: §nhttps://discord.gg/apexrealm'))
                return 1
            })
    )
})
