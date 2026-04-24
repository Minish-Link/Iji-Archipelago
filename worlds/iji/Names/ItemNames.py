from typing import List

Stat_Health = "Health Stat"
Stat_Attack = "Attack Stat"
Stat_Assimilate = "Assimilate Stat"
Stat_Strength = "Strength Stat"
Stat_Crack = "Crack Stat"
Stat_Tasen = "Tasen Stat"
Stat_Komato = "Komato Stat"

Sector_Access: List[str] = [
    "Progressive Sector Access",
    "Sector 1 Access",
    "Sector 2 Access",
    "Sector 3 Access",
    "Sector 4 Access",
    "Sector 5 Access",
    "Sector 6 Access",
    "Sector 7 Access",
    "Sector 8 Access",
    "Sector 9 Access",
    "Sector X Access"
]

Ribbon = "Ribbon"
Supercharge = "Supercharge"

Special_Health = "SUPPRESSION"
Special_Attack = "IMPROVED AUTOLOADING"
Special_Assimilate = "ADVANCED RECOVERY"
Special_Strength = "CYBERNETIC ENDURANCE"
Special_Crack = "ELECTRONIC MASTERY"
Special_Tasen = "VENGEANCE"
Special_Komato = "GLORY"

Filler: List[str] = [
    "Health Pickup",
    "Armor Pickup",
    "Nano Pickup",
    "Machine Ammo",
    "Rocket Ammo",
    "MPFB Ammo",
    "Pulse Ammo",
    "Shock Ammo",
    "CFIS Ammo",
    "Nano Overload",
    "Bundle of Ammo"
    "Can of Soda"
]

NormalTraps: List[str] = [
    "Rocket to the Face",  # Fires an enemy rocket directly at Iji
    # Sends as 'Rocket Trap'
    "Blits Nest",  # Spawns a group of Blits at Iji's location that deal contact damage.
    # Sends as 'Blits Trap'. From 'Bee Trap' and 'Buyon Trap', 'Fire Trap', 'Burn Trap', 'Poison Mushroom',
    # 'Poison Trap', 'Tarr Trap'
    "Null Drive",  # Randomly swaps background images until the game is closed, and shuffles sprites on some objects
    # Sends as 'Null Drive Trap'. From 'Chaos Trap', '144p Trap', 'Crystal Trap', 'Fracture Trap', 'SvC Effect'
    "Turbo Mode",  # Doubles the game's speed for a while.
    # Sends as 'Fast Trap', From 'Metronome Trap'
    "Power Nap",  # Knocks Iji unconscious for 10 seconds.
    # Sends as 'Sleep Trap', From 'Stun Trap'
    "Clown Shoes",  # Enables Clown Mode for a minute, making Iji's shoes squeaky and gives her portrait a clown nose.
    # Sends as 'Clown Trap', From 'Laughter Trap', 'Pie Trap'
    "Banana",  # Spawns an explosive banana at the player's position
    # Sends as 'Banana Trap'. From 'Bomb' and 'Bomb Trap'
    "Assassin",  # Spawns a Komato Assasin that does not drop any XP when defeated.
    # Sends as 'Assassin Trap', 'Gooey Bag', 'Ninja Trap'
    "Logbook",  # Forces the player to read an unskippable Logbook.
    # Sends as 'Literature Trap', 'Ghost Chat', 'Phone Trap', 'Spam Trap', 'Text Trap', 'Trivia Trap'
]

TrapLinks: List[str] = [
    "Scream", # Causes Iji to scream, as though she had been killed.
    # From 'Aaa Trap', 'Syntax Jumpscare Trap'
    "Missile Pony", # Forces the player to restart the current level, but in Horsegun mode.
    # From 'Animal Bonus Trap', 'Ranch Trap'
    "Berserker", # Spawns a Komato Berserker to spawn at the player's location.
    # From 'Army Trap', 'Ghost', 'Police Trap', 'Thwimp Trap'
    "Haircut", # Replaces Iji's sprite with one that has no hair for a while.
    # From 'Bald Trap'
    "Banana Peel", # Spawns a banana and trips Iji.
    # From 'Banana Peel Trap'
    "reallyjoelsdad", # Gives nearby enemies the same power as those in reallyjoelsdad mode.
    # From 'Banner Trap', 'Enchantment Trap'
    "Phantom Hammer", # Instantly kills Iji.
    # From 'Blue Balls Curse', 'Instant Death Trap'
    "Bonk", # Same effect as Power Nap, but with an added Bonk sound effect.
    # From 'Bonk Trap'
    "Crack Minigame", # Forces Iji to play a level 10 cracking minigame. Failure causes her to explode, dealing 2 damage.
    # From 'Fishing Trap', 'Input Sequence Trap', 'Light Up Path Trap', 'Math Quiz Trap',
    # 'Monkey Mash Trap', 'Number Sequence Trap', 'Snake Trap'
    "Slow Mode", # Halves the game's speed for 30 seconds.
    # From 'Bullet Time Trap', 'Frame Slime Trap', 'PowerPoint Trap', 'Underwater Trap'
    "Time Stop", # Forces the game to run at 1 frame per second for 5 seconds.
    # From 'Chaos Control Trap', 'Freeze Trap', 'Frost Trap', 'Frozen Trap', 'Bubble Trap'
    "Alien Vitality", # Increases the health of bosses you fight and makes them harder if able. This effect never expires.
    # From 'Chart Modifier Trap', 'Curse Trap, 'Cursed Ball Trap'
    "Otherworldly Foes", # Spawns random enemies from Sector Z somewhat near Iji.
    # From 'Chaser Trap', 'Fishin Boo Trap', 'Fuzzy Trap', 'Enemy Ball Trap'
    "Forced Reboot", # Performs a Nanofield reboot, resetting all of Iji's stats to 1 and refunding the points.
    # From 'Clear Image Trap'
    "Reverse Controls", # Reverses the player's directional inputs for a while.
    # From 'Confound Trap', 'Confuse Trap', 'Confusion Trap', 'Fear Trap', 'Gas Trap', 'Inverted Mouse Trap', 'Mirror Trap',
    # 'Reverse Controls Trap', 'Reverse Trap'
    "Cutscene", # After the player leaves their current Sector, by any means, they watch an unskippable cutscene.
    # From 'Cutscene Trap'
    "Nanofield Malfunction", # Electrocutes Iji, like an Annihilator, dealing 3 damage and sending her flying backward.
    # From 'Damage Trap', 'Electrocution Trap', 'Squash Trap'
    "Zoom Out", # Resizes the window to be 1/4 its normal size for a while.
    # From 'Deisometric Trap', 'Fish Eye Trap', 'Pixelate Trap', 'Pixellation Trap', 'Zoom Out Trap', 'Zoom Trap'
    "No Ammo", # Sets all of Iji's ammo to 0.
    # From 'Depletion Trap', 'Dry Trap', 'Energy Drain Trap', 'Mana Drain Trap'
    "Locked Knees", # Prevents Iji from being able to jump or duck for a while.
    # From 'Disable A Trap', 'Honey Trap', 'Sticky Floor Trap'
    "Jammed Weapon", # Prevents Iji from firing her weapon for a while.
    # From 'Disable B Trap', 'Disarm Trap', 'No Vac Trap'
    "Firewall", # Disables Iji's ability to interface with/crack objects and enemies for a while
    # From 'Disable C Up Trap'
    "Weapon Lock", # Prevents Iji from switching her current weapon, or from switching to Passive mode.
    # From 'Disable Tag Trap', 'Sticky Hands Trap', 'Paralyze Trap', 'Paralysis Trap'
    "Skip Leg Day", # Prevents Iji from being able to kick for a while.
    # From 'Disable Z Trap'
    "Sudden Death", # For a minute, sets Iji to 1 health and prevents her from getting more.
    # From 'Double Damage', 'Instant Crystal Trap', 'One Hit KO'
    "Easter Egg", # Spawns an Easter Egg at Iji's position.
    # From 'Egg Trap'
    "Pause", # Pauses the game for you.
    # From 'Eject Trap'
    "Empty Boxes", # Forces every security box in the current sector to not reward any items when opened.
    # From 'Empty Item Box Trap'
    "Weapon Inefficiency", # For a while, using your weapons will consume twice as much ammo.
    # From 'Expensive Stocks', 'Market Crash Trap'
    "MPFB to the Face", # Fires a series of MPFB projectiles directly at Iji.
    # From 'Explosion Trap', 'Meteor Trap'
    "Null Drive Madness", # Same effect as Null Drive trap, but triggers every second for 30 seconds.
    # From 'Extreme Chaos Mode'
    "Sector Complete...?", # Causes the camera to display a fade to black, then returns to normal a second later.
    # From 'Fake Transition'
    "Moon Walk", # Flips Iji's sprite horizontally for a while
    # From 'Flip Horizontal Trap', 'Flip Trap'
    "Hand Stand", # Flips Iji's sprite vertically for a while
    # From 'Flip Vertical Trap', Screen Flip Trap'
    "Pacifism", # Forces Iji to swap to Passive Mode and prevents switching back for a while.
    # From 'Frog Trap'
    "Weapon Swap", # Switches Iji's weapon to a random one, then prevents her from switching for a while.
    # From 'Gadget Shuffle Trap', 'Swap Trap', 'Tool Swap Trap'
    "Timer", # Starts a timer, identical to the one in Ultimortal difficulty, which kills Iji when it expires.
    # From 'Get Out Trap', 'Home Trap', 'Impatience Trap', 'Resistance Trap', 'Time Limit', 'Time Warp Trap',
    # 'Timer Trap'
    "Fast Fall", # For a while, Iji's gravity is drastically increased when she's falling.
    # From 'Gravity Trap', 'Iron Boots Trap'
    "Alert", # Plays a sound effect of a random enemy spotting Iji.
    # From 'Hey! Trap'
    "Happy Feet", # Forces Iji to constantly jump for a short period of time.
    # From 'Hiccup Trap', 'Jump Trap', 'Jumping Jacks Trap', 'Icy Hot Pants Trap', 'Spring Trap'
    "Autowalk Protocol", # For a minute, Iji will be forced to constantly walk forward.
    # From 'Ice Floor Trap', 'Ice Trap'
    "Silhouette", # Turns Iji into a completely black silhouette for a while.
    # From 'Invert Colors Trap', 'Spooky Time'
    "Full Invisibilty", # Turns Iji completely invisible for a while.
    # From 'Invisiball Trap', 'Invisible Trap', 'Invisibility Trap', 'Paper Trap'
    "Fireworks", # Detonates all pickups on screen, potentially dealing damage to Iji.
    # From 'Items to Bombs'
    "Hacked by Yukabacera, Loser", # Forces Iji to use random inputs for a short while.
    # From 'My Turn! Trap', 'Posession Trap', 'Control Ball Trap', 'Controller Drift Trap'
    "Vulnerability", # Sets Iji's current armor to 1.
    # From 'No Guarding'
    "No Recovery", # Removes all health and armor pickups from the current sector.
    # From 'No Petals',
    "Exhaustion", # Exhausts all checkpoints in the current sector.
    # From 'No Revivals', 'No Stocks'
    "Shocksplinter to the Face", # Fires an enemy Shocksplinter shot directly at Iji
    # From 'Nut Trap'
    "Chat with Dan", # Forces a dialogue box containing a random unskippable conversation with Dan to appear
    # From 'OmoTrap', 'Help Trap', 'Tip Trap', 'Tutorial Trap'
    "Spawn Dan", # Spawns a Dan object that does nothing near Iji.
    # From 'Person Trap'
    "Hero3D", # Forces Iji to stop what she's doing and play Hero3D for a minute.
    # From 'Pinball Trap', 'Breakout Trap', 'Pokemon Count Trap', 'Pokemon Trivia Trap', 'PONG Challenge', 'Pong Trap',
    # 'UNO Challenge'
    "Slip", # Harmlessly knocks Iji to the ground.
    # From 'Push Trap', 'Slip Trap', 'Whoops! Trap'
    "Max Scramble", # For the next few minutes, all text is scrambled to the maximum degree.
    # From 'Radiation Trap',
    "Mystery Item", # Activates the effect of a random Trap or Filler item (Most likely to be a Trap)
    # From 'Random Status Trap'
    "Ragebomb", # Spawns Tor's Ragebomb projectile nearby, white explodes into a burst of cluster bombs.
    # From 'Rockfall Trap'
    "Rumble", # Causes the screen to shake violently.
    # From 'Shake Trap'
    "Shuffle Stats", # Reassign the Iji's currently spent stat points randomly.
    # From 'Shuffle Trap'
    "Tyrian Claw", # Spawns a burst of Tor's purple spinning projectiles some distance away from Iji
    # From 'Spike Ball Trap'
    "Total Darkness", # Limits your vision to the area immediately around Iji.
    # From 'Space Trap', 'Spotlight Trap', 'Sandstorm Trap'
    "Warpback", # Teleports the player back to the start of the sector or their last checkpoint
    # From 'Teleport Trap'
    "Tiniji", # Makes Iji tiny for a while.
    # From 'Tiny Trap'
    "Fractal Rockets to the Face", # Fires a giant rocket that splits into multiple rockets toward Iji.
    # From 'TNT Barrel Trap', 'TNT Trap'
    "Undo", # The stat Iji most recently increased is decreased by 1 level and the point is refunded.
    # From 'Undo Trap'
    "Well Done", # Spawns floating text saying "Well Done!"
    # From 'Well Done Trap'
    "Fullscreen", # Forces the game to enter full screen for a bit
    # From 'W I D E Trap', 'Zoom In Trap'
    "Spin", # Iji starts spinning for a while.
    # From 'Whirlpool Trap', 'Camera Rotate Trap'
]

Traps: List[str] = NormalTraps + TrapLinks

Debug = "Fire Anytime"
Upgrade_Jump = "Jump Upgrade"
Upgrade_Armor = "Armor Upgrade"
Glitch = "Glitches"

Weapons: List[str] = [
    "Null Driver",
    "Shotgun",
    "Machine Gun",
    "Rocket Launcher",
    "MPFB Devastator",
    "Resonance Detonator",
    "Pulse Cannon",
    "Shocksplinter",
    "Cyclic Fusion Ignition System",
    "Buster Gun",
    "Splintergun",
    "Spread Rockets",
    "Nuke",
    "Resonance Reflector",
    "Hyper Pulse",
    "Plasma Cannon",
    "Velocithor V2-10",
    "Banana Gun",
    "Massacre"
]

Checkpoints: List[str] = [
    "Sector 2 - Checkpoint",
    "Sector 3 - Checkpoint",
    "Sector 4 - Checkpoint",
    "Sector 5 - Checkpoint",
    "Sector 6 - Checkpoint",
    "Sector 7 - First Checkpoint",
    "Sector 7 - Second Checkpoint",
    "Sector 8 - Checkpoint",
    "Sector 9 - First Checkpoint",
    "Sector 9 - Second Checkpoint",
    "Sector X - First Checkpoint",
    "Sector X - Second Checkpoint"
]

StrengthDoorLevels: List[List[str]] = [
    [
    "Progressive Shield Doors",
    "Resistance 1 Doors",
    "Resistance 2 Doors",
    "Resistance 3 Doors",
    "Resistance 4 Doors",
    "Resistance 5 Doors",
    "Resistance 6 Doors",
    "Resistance 7 Doors",
    "Resistance 8 Doors",
    "Resistance 9 Doors",
    "Resistance 10 Doors",
    "Resistance 15+ Doors"
    ],
    [
    "Sector 1 Progressive Shield Doors",
    "Sector 1 Resistance 1 Doors",
    "Sector 1 Resistance 2 Doors",
    "Sector 1 Resistance 3 Doors",
    "Sector 1 Resistance 4 Doors",
    "Sector 1 Resistance 5 Doors",
    "Sector 1 Resistance 6 Doors",
    "Sector 1 Resistance 7 Doors",
    "Sector 1 Resistance 8 Doors",
    "Sector 1 Resistance 9 Doors",
    "Sector 1 Resistance 10 Doors",
    "Sector 1 Resistance 15+ Doors"
    ],
    [
    "Sector 2 Progressive Shield Doors",
    "Sector 2 Resistance 1 Doors",
    "Sector 2 Resistance 2 Doors",
    "Sector 2 Resistance 3 Doors",
    "Sector 2 Resistance 4 Doors",
    "Sector 2 Resistance 5 Doors",
    "Sector 2 Resistance 6 Doors",
    "Sector 2 Resistance 7 Doors",
    "Sector 2 Resistance 8 Doors",
    "Sector 2 Resistance 9 Doors",
    "Sector 2 Resistance 10 Doors",
    "Sector 2 Resistance 15+ Doors"
    ],
    [
    "Sector 3 Progressive Shield Doors",
    "Sector 3 Resistance 1 Doors",
    "Sector 3 Resistance 2 Doors",
    "Sector 3 Resistance 3 Doors",
    "Sector 3 Resistance 4 Doors",
    "Sector 3 Resistance 5 Doors",
    "Sector 3 Resistance 6 Doors",
    "Sector 3 Resistance 7 Doors",
    "Sector 3 Resistance 8 Doors",
    "Sector 3 Resistance 9 Doors",
    "Sector 3 Resistance 10 Doors",
    "Sector 3 Resistance 15+ Doors"
    ],
    [
    "Sector 4 Progressive Shield Doors",
    "Sector 4 Resistance 1 Doors",
    "Sector 4 Resistance 2 Doors",
    "Sector 4 Resistance 3 Doors",
    "Sector 4 Resistance 4 Doors",
    "Sector 4 Resistance 5 Doors",
    "Sector 4 Resistance 6 Doors",
    "Sector 4 Resistance 7 Doors",
    "Sector 4 Resistance 8 Doors",
    "Sector 4 Resistance 9 Doors",
    "Sector 4 Resistance 10 Doors",
    "Sector 4 Resistance 15+ Doors"
    ],
    [
    "Sector 5 Progressive Shield Doors",
    "Sector 5 Resistance 1 Doors",
    "Sector 5 Resistance 2 Doors",
    "Sector 5 Resistance 3 Doors",
    "Sector 5 Resistance 4 Doors",
    "Sector 5 Resistance 5 Doors",
    "Sector 5 Resistance 6 Doors",
    "Sector 5 Resistance 7 Doors",
    "Sector 5 Resistance 8 Doors",
    "Sector 5 Resistance 9 Doors",
    "Sector 5 Resistance 10 Doors",
    "Sector 5 Resistance 15+ Doors"
    ],
    [
    "Sector 6 Progressive Shield Doors",
    "Sector 6 Resistance 1 Doors",
    "Sector 6 Resistance 2 Doors",
    "Sector 6 Resistance 3 Doors",
    "Sector 6 Resistance 4 Doors",
    "Sector 6 Resistance 5 Doors",
    "Sector 6 Resistance 6 Doors",
    "Sector 6 Resistance 7 Doors",
    "Sector 6 Resistance 8 Doors",
    "Sector 6 Resistance 9 Doors",
    "Sector 6 Resistance 10 Doors",
    "Sector 6 Resistance 15+ Doors"
    ],
    [
    "Sector 7 Progressive Shield Doors",
    "Sector 7 Resistance 1 Doors",
    "Sector 7 Resistance 2 Doors",
    "Sector 7 Resistance 3 Doors",
    "Sector 7 Resistance 4 Doors",
    "Sector 7 Resistance 5 Doors",
    "Sector 7 Resistance 6 Doors",
    "Sector 7 Resistance 7 Doors",
    "Sector 7 Resistance 8 Doors",
    "Sector 7 Resistance 9 Doors",
    "Sector 7 Resistance 10 Doors",
    "Sector 7 Resistance 15+ Doors"
    ],
    [
    "Sector 8 Progressive Shield Doors",
    "Sector 8 Resistance 1 Doors",
    "Sector 8 Resistance 2 Doors",
    "Sector 8 Resistance 3 Doors",
    "Sector 8 Resistance 4 Doors",
    "Sector 8 Resistance 5 Doors",
    "Sector 8 Resistance 6 Doors",
    "Sector 8 Resistance 7 Doors",
    "Sector 8 Resistance 8 Doors",
    "Sector 8 Resistance 9 Doors",
    "Sector 8 Resistance 10 Doors",
    "Sector 8 Resistance 15+ Doors"
    ],
    [
    "Sector 9 Progressive Shield Doors",
    "Sector 9 Resistance 1 Doors",
    "Sector 9 Resistance 2 Doors",
    "Sector 9 Resistance 3 Doors",
    "Sector 9 Resistance 4 Doors",
    "Sector 9 Resistance 5 Doors",
    "Sector 9 Resistance 6 Doors",
    "Sector 9 Resistance 7 Doors",
    "Sector 9 Resistance 8 Doors",
    "Sector 9 Resistance 9 Doors",
    "Sector 9 Resistance 10 Doors",
    "Sector 9 Resistance 15+ Doors"
    ],
    [
    "Sector X Progressive Shield Doors",
    "Sector X Resistance 1 Doors",
    "Sector X Resistance 2 Doors",
    "Sector X Resistance 3 Doors",
    "Sector X Resistance 4 Doors",
    "Sector X Resistance 5 Doors",
    "Sector X Resistance 6 Doors",
    "Sector X Resistance 7 Doors",
    "Sector X Resistance 8 Doors",
    "Sector X Resistance 9 Doors",
    "Sector X Resistance 10 Doors",
    "Sector X Resistance 15+ Doors"
    ],
]

CrackDoorLevels: List[List[str]] = [
    [
    "Progressive Security Doors",
    "Security 1 Doors",
    "Security 2 Doors",
    "Security 3 Doors",
    "Security 4 Doors",
    "Security 5 Doors",
    "Security 6 Doors",
    "Security 7 Doors",
    "Security 8 Doors",
    "Security 9 Doors",
    "Security 10 Doors",
    "Security 15+ Doors"
    ],
    [
    "Sector 1 Progressive Security Doors",
    "Sector 1 Security 1 Doors",
    "Sector 1 Security 2 Doors",
    "Sector 1 Security 3 Doors",
    "Sector 1 Security 4 Doors",
    "Sector 1 Security 5 Doors",
    "Sector 1 Security 6 Doors",
    "Sector 1 Security 7 Doors",
    "Sector 1 Security 8 Doors",
    "Sector 1 Security 9 Doors",
    "Sector 1 Security 10 Doors",
    "Sector 1 Security 15+ Doors"
    ],
    [
    "Sector 2 Progressive Security Doors",
    "Sector 2 Security 1 Doors",
    "Sector 2 Security 2 Doors",
    "Sector 2 Security 3 Doors",
    "Sector 2 Security 4 Doors",
    "Sector 2 Security 5 Doors",
    "Sector 2 Security 6 Doors",
    "Sector 2 Security 7 Doors",
    "Sector 2 Security 8 Doors",
    "Sector 2 Security 9 Doors",
    "Sector 2 Security 10 Doors",
    "Sector 2 Security 15+ Doors"
    ],
    [
    "Sector 3 Progressive Security Doors",
    "Sector 3 Security 1 Doors",
    "Sector 3 Security 2 Doors",
    "Sector 3 Security 3 Doors",
    "Sector 3 Security 4 Doors",
    "Sector 3 Security 5 Doors",
    "Sector 3 Security 6 Doors",
    "Sector 3 Security 7 Doors",
    "Sector 3 Security 8 Doors",
    "Sector 3 Security 9 Doors",
    "Sector 3 Security 10 Doors",
    "Sector 3 Security 15+ Doors"
    ],
    [
    "Sector 4 Progressive Security Doors",
    "Sector 4 Security 1 Doors",
    "Sector 4 Security 2 Doors",
    "Sector 4 Security 3 Doors",
    "Sector 4 Security 4 Doors",
    "Sector 4 Security 5 Doors",
    "Sector 4 Security 6 Doors",
    "Sector 4 Security 7 Doors",
    "Sector 4 Security 8 Doors",
    "Sector 4 Security 9 Doors",
    "Sector 4 Security 10 Doors",
    "Sector 4 Security 15+ Doors"
    ],
    [
    "Sector 5 Progressive Security Doors",
    "Sector 5 Security 1 Doors",
    "Sector 5 Security 2 Doors",
    "Sector 5 Security 3 Doors",
    "Sector 5 Security 4 Doors",
    "Sector 5 Security 5 Doors",
    "Sector 5 Security 6 Doors",
    "Sector 5 Security 7 Doors",
    "Sector 5 Security 8 Doors",
    "Sector 5 Security 9 Doors",
    "Sector 5 Security 10 Doors",
    "Sector 5 Security 15+ Doors"
    ],
    [
    "Sector 6 Progressive Security Doors",
    "Sector 6 Security 1 Doors",
    "Sector 6 Security 2 Doors",
    "Sector 6 Security 3 Doors",
    "Sector 6 Security 4 Doors",
    "Sector 6 Security 5 Doors",
    "Sector 6 Security 6 Doors",
    "Sector 6 Security 7 Doors",
    "Sector 6 Security 8 Doors",
    "Sector 6 Security 9 Doors",
    "Sector 6 Security 10 Doors",
    "Sector 6 Security 15+ Doors"
    ],
    [
    "Sector 7 Progressive Security Doors",
    "Sector 7 Security 1 Doors",
    "Sector 7 Security 2 Doors",
    "Sector 7 Security 3 Doors",
    "Sector 7 Security 4 Doors",
    "Sector 7 Security 5 Doors",
    "Sector 7 Security 6 Doors",
    "Sector 7 Security 7 Doors",
    "Sector 7 Security 8 Doors",
    "Sector 7 Security 9 Doors",
    "Sector 7 Security 10 Doors",
    "Sector 7 Security 15+ Doors"
    ],
    [
    "Sector 8 Progressive Security Doors",
    "Sector 8 Security 1 Doors",
    "Sector 8 Security 2 Doors",
    "Sector 8 Security 3 Doors",
    "Sector 8 Security 4 Doors",
    "Sector 8 Security 5 Doors",
    "Sector 8 Security 6 Doors",
    "Sector 8 Security 7 Doors",
    "Sector 8 Security 8 Doors",
    "Sector 8 Security 9 Doors",
    "Sector 8 Security 10 Doors",
    "Sector 8 Security 15+ Doors"
    ],
    [
    "Sector 9 Progressive Security Doors",
    "Sector 9 Security 1 Doors",
    "Sector 9 Security 2 Doors",
    "Sector 9 Security 3 Doors",
    "Sector 9 Security 4 Doors",
    "Sector 9 Security 5 Doors",
    "Sector 9 Security 6 Doors",
    "Sector 9 Security 7 Doors",
    "Sector 9 Security 8 Doors",
    "Sector 9 Security 9 Doors",
    "Sector 9 Security 10 Doors",
    "Sector 9 Security 15+ Doors"
    ],
    [
    "Sector X Progressive Security Doors",
    "Sector X Security 1 Doors",
    "Sector X Security 2 Doors",
    "Sector X Security 3 Doors",
    "Sector X Security 4 Doors",
    "Sector X Security 5 Doors",
    "Sector X Security 6 Doors",
    "Sector X Security 7 Doors",
    "Sector X Security 8 Doors",
    "Sector X Security 9 Doors",
    "Sector X Security 10 Doors",
    "Sector X Security 15+ Doors"
    ],
]

TerminalDoorGroups: List[str] = [
    "Terminal Doors",
    "Sector 1 Terminal Doors",
    "Sector 2 Terminal Doors",
    "Sector 3 Terminal Doors",
    "Sector 4 Terminal Doors",
    "Sector 5 Terminal Doors",
    "Sector 6 Terminal Doors",
    "Sector 7 Terminal Doors",
    "Sector 8 Terminal Doors",
    "Sector 9 Terminal Doors",
    "Sector X Terminal Doors"
]