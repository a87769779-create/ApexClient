StartupEvents.registry('item', event => {
    event.create('copper_coin').displayName('§cМедная Монета').texture('minecraft:item/copper_ingot').glow(false)
    event.create('silver_coin').displayName('§bСеребряная Монета').texture('minecraft:item/iron_nugget').glow(false)
    event.create('gold_coin').displayName('§eЗолотая Монета').texture('minecraft:item/gold_nugget').glow(true)
    event.create('diamond_coin').displayName('§bАлмазная Монета').texture('minecraft:item/diamond').glow(true)
})
