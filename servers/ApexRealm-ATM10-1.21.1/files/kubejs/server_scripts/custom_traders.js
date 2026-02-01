// server_scripts/custom_traders.js

/*
    Скрипт для призыва кастомного торговца.
    Использование: /summon_trader
    
    Торговец будет продавать предметы за монеты (kubejs:copper_coin, etc.)
    Вы можете менять список товаров (trades) ниже.
*/

ServerEvents.commandRegistry(event => {
    const { commands: Commands, arguments: Arguments } = event;

    event.register(
        Commands.literal('summon_trader')
            .requires(s => s.hasPermission(2)) // Только для админов
            .executes(c => {
                let player = c.source.player;
                if (!player) return 0;

                let level = player.level;
                let pos = player.position();

                // Создаем жителя
                let villager = level.createEntity('minecraft:villager');
                villager.setPosition(pos.x, pos.y, pos.z);
                villager.setNoAi(true); // Стоит на месте
                villager.setInvulnerable(true); // Неуязвимый
                villager.setCustomName(Text.of("§6§lТорговец Редкостями")); // Золотое имя

                // Настраиваем профессию (визуально)
                villager.mergeNbt({
                    VillagerData: {
                        profession: "minecraft:wandering_trader",
                        level: 5,
                        type: "minecraft:plains"
                    },
                    Offers: {
                        Recipes: [
                            // === ОБМЕН ВАЛЮТЫ (Продажа ресурсов) ===
                            {
                                buy: { id: "minecraft:cobblestone", Count: 64 },
                                sell: { id: "kubejs:copper_coin", Count: 1 },
                                maxUses: 9999,
                                xp: 0
                            },
                            {
                                buy: { id: "minecraft:dirt", Count: 64 },
                                sell: { id: "kubejs:copper_coin", Count: 1 },
                                maxUses: 9999,
                                xp: 0
                            },
                            {
                                buy: { id: "minecraft:iron_ingot", Count: 32 },
                                sell: { id: "kubejs:silver_coin", Count: 1 },
                                maxUses: 9999,
                                xp: 0
                            },
                            {
                                buy: { id: "minecraft:gold_ingot", Count: 16 },
                                sell: { id: "kubejs:silver_coin", Count: 1 },
                                maxUses: 9999,
                                xp: 0
                            },
                            {
                                buy: { id: "minecraft:diamond", Count: 1 },
                                sell: { id: "kubejs:silver_coin", Count: 5 },
                                maxUses: 9999,
                                xp: 0
                            },
                            {
                                buy: { id: "minecraft:emerald", Count: 1 },
                                sell: { id: "kubejs:silver_coin", Count: 5 },
                                maxUses: 9999,
                                xp: 0
                            },

                            // === КОНВЕРТАЦИЯ МОНЕТ ===
                            {
                                buy: { id: "kubejs:copper_coin", Count: 64 },
                                sell: { id: "kubejs:silver_coin", Count: 1 },
                                maxUses: 9999,
                                xp: 0
                            },
                            {
                                buy: { id: "kubejs:silver_coin", Count: 1 },
                                sell: { id: "kubejs:copper_coin", Count: 64 },
                                maxUses: 9999,
                                xp: 0
                            },
                            {
                                buy: { id: "kubejs:silver_coin", Count: 64 },
                                sell: { id: "kubejs:gold_coin", Count: 1 },
                                maxUses: 9999,
                                xp: 0
                            },
                            {
                                buy: { id: "kubejs:gold_coin", Count: 1 },
                                sell: { id: "kubejs:silver_coin", Count: 64 },
                                maxUses: 9999,
                                xp: 0
                            },

                            // === МАГАЗИН (Покупка предметов) ===
                            // Еда
                            {
                                buy: { id: "kubejs:copper_coin", Count: 5 },
                                sell: { id: "minecraft:cooked_beef", Count: 16 },
                                maxUses: 9999,
                                xp: 0
                            },
                            // Блоки
                            {
                                buy: { id: "kubejs:copper_coin", Count: 1 },
                                sell: { id: "minecraft:oak_log", Count: 16 },
                                maxUses: 9999,
                                xp: 0
                            },
                            {
                                buy: { id: "kubejs:copper_coin", Count: 1 },
                                sell: { id: "minecraft:stone", Count: 32 },
                                maxUses: 9999,
                                xp: 0
                            },
                            // Редкие ресурсы
                            {
                                buy: { id: "kubejs:silver_coin", Count: 10 }, // Цена покупки выше продажи
                                sell: { id: "minecraft:diamond", Count: 1 },
                                maxUses: 10,
                                xp: 2
                            },
                            {
                                buy: { id: "kubejs:gold_coin", Count: 5 },
                                sell: { id: "minecraft:netherite_ingot", Count: 1 },
                                maxUses: 5,
                                xp: 5
                            },
                            {
                                buy: { id: "kubejs:gold_coin", Count: 10 },
                                sell: { id: "allthemodium:allthemodium_nugget", Count: 1 },
                                maxUses: 3,
                                xp: 10
                            }
                        ]
                    }
                });

                villager.spawn();
                player.tell("§aТорговец успешно призван!");
                return 1;
            })
    );
});
