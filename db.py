# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.dbsparta
#
# # 코딩 시작
# doc = { 'name' : 'bobby', 'age' : 21 }
# db.users.insert_one(doc)
import pymongo
from pymongo import MongoClient

ip ='mongodb://antitest:anti1234test@54.180.85.88'
port = 27017

client = pymongo.MongoClient('localhost', port)
db = client.anti


def insert():
    # db.poster.delete_many({})
    db.wannabe.delete_many({})
    db.story.delete_many({})
    wordlist = [
        {"word": "Loving", "path": "../static/mapping/Loving.png"},
        {"word": "Dear", "path": "../static/mapping/Loving.png"},
        {"word": "Tender", "path": "../static/mapping/Loving.png"},
        {"word": "Fond", "path": "../static/mapping/Loving.png"},
        {"word": "Doting", "path": "../static/mapping/Loving.png"},
        {"word": "Lovely", "path": "../static/mapping/Loving.png"},
        {"word": "Classy", "path": "../static/mapping/Classy.png"},
        {"word": "High class", "path": "../static/mapping/Classy.png"},
        {"word": "Superior","path":"../static/mapping/Classy.png"},
        {"word": "Upmarket", "path": "../static/mapping/Classy.png"},
        {"word": "Stylish", "path": "../static/mapping/Classy.png"},
	    {"word": "Friendly", "path": "../static/mapping/Friendly.png"},
        {"word": "Neighbourly", "path": "../static/mapping/Friendly.png"},
        {"word": "Helpful", "path": "../static/mapping/Friendly.png"},
        {"word": "Amiable", "path": "../static/mapping/Friendly.png"},
        {"word": "Sympathetic", "path": "../static/mapping/Friendly.png"},
        {"word": "Progressive", "path": "../static/mapping/Progressive.png"},
        {"word": "Liberal", "path": "../static/mapping/Progressive.png"},
        {"word": "Advanced", "path": "../static/mapping/Progressive.png"},
        {"word": "Revolutionary","path":"../static/mapping/Progressive.png"},
        {"word": "Avant garde", "path": "../static/mapping/Progressive.png"},
        {"word": "Sporty", "path": "../static/mapping/Sporty.png"},
        {"word": "Athletic", "path": "../static/mapping/Sporty.png"},
        {"word": "Outdoor", "path": "../static/mapping/Sporty.png"},
        {"word": "Energetic", "path": "../static/mapping/Sporty.png"},
        {"word": "Peaceful", "path": "../static/mapping/Peaceful.png"},
        {"word": "At peace", "path": "../static/mapping/Peaceful.png"},
        {"word": "Harmonious", "path": "../static/mapping/Peaceful.png"},
        {"word": "Amicable", "path": "../static/mapping/Peaceful.png"},
        {"word": "Hostile", "path": "../static/mapping/Peaceful.png"},
        {"word": "Rich","path":"../static/mapping/Rich.png"},
        {"word": "Affluent", "path": "../static/mapping/Rich.png"},
        {"word": "Prosperous", "path": "../static/mapping/Rich.png"},
	    {"word": "Moneyed", "path": "../static/mapping/Rich.png"},
        {"word": "Wealthy", "path": "../static/mapping/Rich.png"},
        {"word": "Loaded", "path": "../static/mapping/Rich.png"},
        {"word": "Sweet", "path": "../static/mapping/Sweet.png"},
        {"word": "Sugary", "path": "../static/mapping/Sweet.png"},
        {"word": "Icky", "path": "../static/mapping/Sweet.png"},
        {"word": "Cloying", "path": "../static/mapping/Sweet.png"},
        {"word": "Hip", "path": "../static/mapping/Hip.png"},
        {"word": "Hipper","path":"../static/mapping/Hip.png"},
        {"word": "Hippest", "path": "../static/mapping/Hip.png"},
        {"word": "Great", "path": "../static/mapping/Great.png"},
        {"word": "Large", "path": "../static/mapping/Great.png"},
        {"word": "Big", "path": "../static/mapping/Great.png"},
        {"word": "Huge", "path": "../static/mapping/Great.png"},
        {"word": "Enormous", "path": "../static/mapping/Great.png"},
        {"word": "Young", "path": "../static/mapping/Young.png"},
        {"word": "Immature", "path": "../static/mapping/Young.png"},
        {"word": "Youthful", "path": "../static/mapping/Young.png"},
        {"word": "Little","path":"../static/mapping/Young.png"},
        {"word": "Junior", "path": "../static/mapping/Young.png"},
        {"word": "Infant", "path": "../static/mapping/Young.png"},
	    {"word": "Strong", "path": "../static/mapping/Strong.png"},
        {"word": "Muscular", "path": "../static/mapping/Strong.png"},
        {"word": "Hardy", "path": "../static/mapping/Strong.png"},
        {"word": "Sturdy", "path": "../static/mapping/Strong.png"},
        {"word": "Burly", "path": "../static/mapping/Strong.png"},
        {"word": "Strapping", "path": "../static/mapping/Strong.png"},
        {"word": "Faithful", "path": "../static/mapping/Faithful.png"},
        {"word": "Committed", "path": "../static/mapping/Faithful.png"},
        {"word": "Constant","path":"../static/mapping/Faithful.png"},
        {"word": "Dedicated", "path": "../static/mapping/Faithful.png"},
        {"word": "Reliable", "path": "../static/mapping/Faithful.png"},
        {"word": "Staunch", "path": "../static/mapping/Faithful.png"},
        {"word": "Funny", "path": "../static/mapping/Funny.png"},
        {"word": "Humorous", "path": "../static/mapping/Funny.png"},
        {"word": "Amusing", "path": "../static/mapping/Funny.png"},
        {"word": "Comic", "path": "../static/mapping/Funny.png"},
        {"word": "Hilarious", "path": "../static/mapping/Funny.png"},
        {"word": "Riotous", "path": "../static/mapping/Funny.png"},
        {"word": "Passionate", "path": "../static/mapping/Passionate.png"},
        {"word": "Eager","path":"../static/mapping/Passionate.png"},
        {"word": "Intense", "path": "../static/mapping/Passionate.png"},
        {"word": "Ardent", "path": "../static/mapping/Passionate.png"},
	    {"word": "Fervent", "path": "../static/mapping/Passionate.png"},
        {"word": "Fair", "path": "../static/mapping/Fair.png"},
        {"word": "Unbiased", "path": "../static/mapping/Fair.png"},
        {"word": "Impartial", "path": "../static/mapping/Fair.png"},
        {"word": "Just", "path": "../static/mapping/Fair.png"},
        {"word": "Reasonable", "path": "../static/mapping/Fair.png"},
        {"word": "Proper", "path": "../static/mapping/Fair.png"},
        {"word": "Cool", "path": "../static/mapping/Cool.png"},
        {"word": "Cold","path":"../static/mapping/Cool.png"},
        {"word": "Chilly", "path": "../static/mapping/Cool.png"},
        {"word": "Nippy", "path": "../static/mapping/Cool.png"},
        {"word": "Unconstrained","path":"../static/mapping/Unconstrained.png"},
        {"word": "Unaffected", "path": "../static/mapping/Unaffected.png"},
        {"word": "Clever", "path": "../static/mapping/Clever.png"},
	    {"word": "Intelligent", "path": "../static/mapping/Clever.png"},
        {"word": "Gifted", "path": "../static/mapping/Clever.png"},
        {"word": "Bright", "path": "../static/mapping/Clever.png"},
        {"word": "Traveling", "path": "../static/mapping/Traveling.png"},
        {"word": "Global", "path": "../static/mapping/Global.png"},
        {"word": "Worldwide", "path": "../static/mapping/Global.png"},
        {"word": "World", "path": "../static/mapping/Global.png"},
        {"word": "International", "path": "../static/mapping/Global.png"},
        {"word": "Universal","path":"../static/mapping/Global.png"},
        {"word": "Healthy", "path": "../static/mapping/Healthy.png"},
        {"word": "Well", "path": "../static/mapping/Healthy.png"},
        {"word": "Git","path":"../static/mapping/Healthy.png"},
        {"word": "In good shape", "path": "../static/mapping/Healthy.png"},
        {"word": "Witty", "path": "../static/mapping/Witty.png"},
	    {"word": "Dull", "path": "../static/mapping/Witty.png"},
        {"word": "Droll", "path": "../static/mapping/Witty.png"},
        {"word": "Whimsical", "path": "../static/mapping/Witty.png"},
        {"word": "Sparkling", "path": "../static/mapping/Witty.png"},
        {"word": "Be Loved", "path": "../static/mapping/Be-Loved.png"},
        {"word": "Valued", "path": "../static/mapping/Be-Loved.png"},
        {"word": "Prized", "path": "../static/mapping/Be-Loved.png"},
        {"word": "Precious", "path": "../static/mapping/Be-Loved.png"},
        {"word": "Darling","path":"../static/mapping/Be-Loved.png"},
        {"word": "Treasured", "path": "../static/mapping/Be-Loved.png"},
        {"word": "Calm", "path": "../static/mapping/Calm.png"},
        {"word": "Sedate", "path": "../static/mapping/Calm.png"},
        {"word": "Self possessed", "path": "../static/mapping/Calm.png"},
        {"word": "Dispassionate", "path": "../static/mapping/Calm.png"},
        {"word": "Famous", "path": "../static/mapping/Famous.png"},
        {"word": "Celebrated", "path": "../static/mapping/Famous.png"},
        {"word": "Interesting", "path": "../static/mapping/Interesting.png"},
        {"word": "Appealing", "path": "../static/mapping/Interesting.png"},
        {"word": "Gripping","path":"../static/mapping/Interesting.png"},
        {"word": "Inspirational", "path": "../static/mapping/Inspirational.png"},
        {"word": "Tough", "path": "../static/mapping/Tough.png"},
	    {"word": "Stout", "path": "../static/mapping/Tough.png"},
        {"word": "Vigorous", "path": "../static/mapping/Tough.png"},
        {"word": "Seasoned", "path": "../static/mapping/Tough.png"},
        {"word": "Cute", "path": "../static/mapping/Cute.png"},
        {"word": "Lovable", "path": "../static/mapping/Cute.png"},
        {"word": "Benevolent", "path": "../static/mapping/Benevolent.png"},
        {"word": "Kindly", "path": "../static/mapping/Benevolent.png"},
        {"word": "Generous", "path": "../static/mapping/Benevolent.png"},
        {"word": "Big hearted","path":"../static/mapping/Benevolent.png"},
        {"word": "Munificent", "path": "../static/mapping/Benevolent.png"},
        {"word": "Unselfish", "path": "../static/mapping/Benevolent.png"},
        {"word": "Ungrudging", "path": "../static/mapping/Benevolent.png"},
        {"word": "Joyful", "path": "../static/mapping/Joyful.png"},
        {"word": "Joyous", "path": "../static/mapping/Joyful.png"},
        {"word": "Well known", "path": "../static/mapping/Well-known.png"},
        {"word": "Noted", "path": "../static/mapping/Well-known.png"},
        {"word": "Prominent", "path": "../static/mapping/Well-known.png"},
        {"word": "Renowned", "path": "../static/mapping/Well-known.png"},
        {"word": "Christian", "path": "../static/mapping/Christian.png"},
        {"word": "Natural","path":"../static/mapping/Natural.png"},
        {"word": "Ordinary", "path": "../static/mapping/Natural.png"},
        {"word": "Typical", "path": "../static/mapping/Natural.png"},
	    {"word": "Everyday", "path": "../static/mapping/Natural.png"},
        {"word": "Smart", "path": "../static/mapping/Smart.png"},
        {"word": "Chic", "path": "../static/mapping/Smart.png"},
        {"word": "Neat", "path": "../static/mapping/Smart.png"},
        {"word": "Snappy", "path": "../static/mapping/Smart.png"},
        {"word": "Natty", "path": "../static/mapping/Smart.png"},
        {"word": "Scruffy", "path": "../static/mapping/Smart.png"},
        {"word": "Knowledgeable", "path": "../static/mapping/Knowledgeable.png"},
        {"word": "Learned","path":"../static/mapping/Knowledgeable.png"},
        {"word": "Educated", "path": "../static/mapping/Knowledgeable.png"},
        {"word": "Conversant", "path": "../static/mapping/Knowledgeable.png"},
        {"word": "Beautiful", "path": "../static/mapping/Beautiful.png"},
        {"word": "Pretty", "path": "../static/mapping/Beautiful.png"},
        {"word": "Pleasant", "path": "../static/mapping/Beautiful.png"},
        {"word": "Fetching", "path": "../static/mapping/Beautiful.png"},
        {"word": "Cheerful", "path": "../static/mapping/Cheerful.png"},
        {"word": "Optimistic", "path": "../static/mapping/Cheerful.png"},
        {"word": "Enthusiastic", "path": "../static/mapping/Cheerful.png"},
        {"word": "Splendid","path":"../static/mapping/Splendid.png"},
        {"word": "Marvellous", "path": "../static/mapping/Splendid.png"},
        {"word": "Unattached", "path": "../static/mapping/Unattached.png"},
	    {"word": "Single", "path": "../static/mapping/Unattached.png"},
        {"word": "Unmarried", "path": "../static/mapping/Unattached.png"},
        {"word": "Brave", "path": "../static/mapping/Brave.png"},
        {"word": "Courageous", "path": "../static/mapping/Brave.png"},
        {"word": "Heroic", "path": "../static/mapping/Brave.png"},
        {"word": "Modest", "path": "../static/mapping/Modest.png"},
        {"word": "Moderate", "path": "../static/mapping/Modest.png"},
        {"word": "Considerate", "path": "../static/mapping/Considerate.png"},
        {"word": "Thoughtful","path":"../static/mapping/Considerate.png"},
        {"word": "Concerned", "path": "../static/mapping/Considerate.png"},
        {"word": "Mindful", "path": "../static/mapping/Considerate.png"},
        {"word": "Caring", "path": "../static/mapping/Considerate.png"},
        {"word": "Polite", "path": "../static/mapping/Considerate.png"},
        {"word": "Respectful", "path": "../static/mapping/Respectful.png"},
        {"word": "Reverent", "path": "../static/mapping/Respectful.png"},
        {"word": "Humble", "path": "../static/mapping/Respectful.png"},
        {"word": "Dutiful", "path": "../static/mapping/Respectful.png"},
        {"word": "Independent", "path": "../static/mapping/Independent.png"},
        {"word": "Separate", "path": "../static/mapping/Independent.png"},
        {"word": "Uncontrolled","path":"../static/mapping/Independent.png"},
        {"word": "Unconstrained", "path": "../static/mapping/Independent.png"},
        {"word": "Radical", "path": "../static/mapping/Radical.png"},
	    {"word": "Extreme", "path": "../static/mapping/Radical.png"},
        {"word": "Complete", "path": "../static/mapping/Radical.png"},
        {"word": "Entire", "path": "../static/mapping/Radical.png"},
        {"word": "Weeping", "path": "../static/mapping/Radical.png"},
        {"word": "Thorough", "path": "../static/mapping/Radical.png"},
        {"word": "Drastic", "path": "../static/mapping/Radical.png"},
        {"word": "Bold", "path": "../static/mapping/Bold.png"},
        {"word": "Fearless", "path": "../static/mapping/Bold.png"},
        {"word": "Enterprising","path":"../static/mapping/Bold.png"},
        {"word": "Courageous", "path": "../static/mapping/Bold.png"},
        {"word": "Lofty","path":"../static/mapping/Dignified.png"},
        {"word": "Noble", "path": "../static/mapping/Dignified.png"},
        {"word": "Courtly", "path": "../static/mapping/Dignified.png"},
	    {"word": "Majestic", "path": "../static/mapping/Dignified.png"},
        {"word": "Kingly", "path": "../static/mapping/Dignified.png"},
        {"word": "Proud", "path": "../static/mapping/Dignified.png"},
        {"word": "Grand", "path": "../static/mapping/Dignified.png"},
        {"word": "Brainy", "path": "../static/mapping/Brainy.png"},
        {"word": "Erudite", "path": "../static/mapping/Brainy.png"},
        {"word": "Highbrow", "path": "../static/mapping/Brainy.png"},
        {"word": "Academic", "path": "../static/mapping/Brainy.png"},
        {"word": "Cultured","path":"../static/mapping/Brainy.png"},
        {"word": "Scholarly", "path": "../static/mapping/Brainy.png"},
        {"word": "Communicative", "path": "../static/mapping/Communicative.png"},
        {"word": "Impressionable","path":"../static/mapping/Communicative.png"},
        {"word": "Sensitive", "path": "../static/mapping/Communicative.png"},
        {"word": "Open-minded", "path": "../static/mapping/Open-minded.png"},
	    {"word": "Balanced", "path": "../static/mapping/Open-minded.png"},
        {"word": "Objective", "path": "../static/mapping/Open-minded.png"},
        {"word": "Tolerant", "path": "../static/mapping/Open-minded.png"},
        {"word": "Receptive", "path": "../static/mapping/Open-minded.png"},
        {"word": "Free", "path": "../static/mapping/Free.png"},
        {"word": "Lots of hair", "path": "../static/mapping/Lots-of-hair.png"},
        {"word": "Strong Minded", "path": "../static/mapping/Strong-Minded.png"},
        {"word": "Firm", "path": "../static/mapping/Strong-Minded.png"},
        {"word": "Resolute","path":"../static/mapping/Strong-Minded.png"},
        {"word": "Purposeful", "path": "../static/mapping/Strong-Minded.png"},
        {"word": "Fearless", "path": "../static/mapping/Strong-Minded.png"},
        {"word": "Warm", "path": "../static/mapping/Warm.png"},
        {"word": "Balmy","path":"../static/mapping/Warm.png"},
        {"word": "Mild", "path": "../static/mapping/Warm.png"},
        {"word": "Temperate", "path": "../static/mapping/Warm.png"},
	    {"word": "Happy", "path": "../static/mapping/Happy.png"},
        {"word": "Thrilled", "path": "../static/mapping/Happy.png"},
        {"word": "Pleased", "path": "../static/mapping/Happy.png"},
        {"word": "Delighted", "path": "../static/mapping/Happy.png"},
        {"word": "Fine", "path": "../static/mapping/Happy.png"},
        {"word": "Pleasant", "path": "../static/mapping/Happy.png"},
        {"word": "Relaxed", "path": "../static/mapping/Relaxed.png"},
        {"word": "Relaxing", "path": "../static/mapping/Relaxed.png"},
        {"word": "Satified","path":"../static/mapping/Relaxed.png"},
        {"word": "Relieve", "path": "../static/mapping/Relaxed.png"},
        {"word": "Relieved", "path": "../static/mapping/Relaxed.png"},
        {"word": "Artistic", "path": "../static/mapping/Artistic.png"},
        {"word": "Eloquent","path":"../static/mapping/Artistic.png"},
        {"word": "Creative", "path": "../static/mapping/Artistic.png"},
        {"word": "Refined", "path": "../static/mapping/Artistic.png"}
    ]
    db.wannabe.insert_many(wordlist)
    stories = [
        {"story": "여성 후배들에게 후원할 수 있는 할머니가 될거야!"},
        {"story":"자립적으로 살아갈 수 있고, 결혼유무와 상관없이 노인들끼리 다양한 커뮤니티에서 어울려서 즐겁게 살며 서로의 애환을 공유하는 동료가 있는 삶을 살고 싶다."},
        {"story":"젊은 세대가 친해지고 싶어할만큼 여전히 흥미롭고 기대고 싶을만큼 현명한 사람이 되어있고 싶어요."},
        {"story":"본업으로 벌만큼 벌어서 당당하게 나름의 여유를 가질수 있는, 옷도 잘입고 귀여우면서 멋쟁이인 할머니가 되고 싶다."},
        {"story": "건강하고 따뜻하고 지혜로운 할머니!"},
        {"story": "행복한 할머니가 되고 싶습니다. 행복하려면 일단 건강해야겠죠. 돈이 많으면 더 좋구요. 그리고 나를 잘 알고 나를 사랑하는 당당하고 주체적인 할머니가 되고싶어요!"},
        {"story": "올바른 어른으로 성숙하더라도 인간적으로는 순수한 사람으로 늙고싶다. 나이가 들어도 열정적이고 도전적이고 사랑에 두려워하지않고 사랑받고 싶은 욕망이 창피하지 않은 사람으로."},
        {"story": "나 하고 싶은 거 다 하고 사는 부자 할머니 하고 싶어요. 돈 다 쓰고 죽을 거라는 각오로 이곳 저곳 다니면서 삶을 즐기고 연하남(!)도 만나는 건강한 부자 할머니!"},
        {"story": "저는 나이를 먹더라도 하고 싶은 일을 겁내지 않고 시도 할 수 있는 할머니이고 싶습니다. 그를 위해 건강하고 여유있으며, 친화력이 있는 사람이고 싶습니다."},
        {"story": "죽을때까지 남한테 손 안벌이고 내 밥벌이 하며 너무 오래 살지도 않고 적당히 좋아하는 사람들과 좋은 술 마시는 할머니가 되고 싶어요!"},
        {"story": "멋있는 할머니가 되고 싶습니다. 많은 여성들에게 영감과 용기를 준 많은 할머니들처럼 저도 존재 자체로 여성들에게 힘이 되는 할머니가 되고 싶네요."},
        {"story": "미완성의 할머니가 되고 싶다. 모든 것이 완성된 노년을 보내고 싶지 않다. 나이가 들어서도 새롭게 배우는 것이 있고, 끊임없이 창작하는 것이 남아있는 미완성이고 싶다."},
        {"story": "흰 백발 숏컷 머리 멋있게 넘기고 레드 립스틱 바르고 싶어요. 그리고 외국어 유창하게 하고 주식 잘하는 똑똑한 할머니. 아침에 예쁘고 맛있는 브런치 먹고 카페가서 맥북으로 작업하고싶어요. 돈많아서 기부도 하고 용돈 턱턱주는 할머니 (손자손녀 아니어도)"},
        {"story": "내 자신의 행복을 지킬 수 있으면서도 타인에게 다정하며, 스스로를 존중하는 만큼 타인을 존중할 수 있는 사람으로 늙어가고 싶다."},
        {"story": "사랑주고 사랑 받을 줄 아는 할머니, 따스함을 전달하는 할머니가 될래요~"},
        {"story": "늙었을때 마음이 성숙하고 좋은 가치관이 풍부한 사람이 되어있으면 좋겠습니다."},
        {"story": "업적을 이루고 돈도 많이 벌어서 주변사람들한테 맛있는 거 사줄 수 있는 할머니가 되고 싶어요!"},
        {"story": "멋진 사람이 되고 싶습니다. 여전히 옷을 좋아하는 사람이고 싶습니다. 스타일 좋은 사람이고 싶어요. 시니어 모델에 도전하는 것도 좋을 것 같아요. 돈이 많아서 베풀 줄 아는 사람. 좋은 사람을 곁에 많이 둔 사람. 여유로운 여행을 즐길 줄 아는 사람. 마음이 잘 통하는 젊은 친구가 있는 것도 특별할 것 같아요. 취미생활이 있었으면 좋겠네요. 이 모든 것을 잘하기 위해선 용기가 필요할 거고 무엇보다 건강해야겠죠. 지금처럼 꾸준히 운동하는 사람이었으면 합니다."},
        {"story": "우선은 할머니, 즉 나이든 여성에서 '여성'보다는 '나이든'에 초점을 맞추고 싶습니다. 나이가 든다는건 나 자신도 죽음에 한걸음 가까워질 뿐 아니라 가족, 친구 등 주변사람들도 하나둘 떠나간다는 의미이기도 합니다. 저는 삶을 지속하는데에 매달리지않고 얼마나 남았을지 모를 앞으로의 살날들을 하루하루 의미있게 보내는데 남은 기력을 사용하는, 나와 내 주변을 맴돌 죽음에 초연할 수 있는 그런 강인한 노인이 되길 원합니다."}

    ]
    db.story.insert_many(stories)
    wordEx = [
        {"word": "Loving"},
        {"word": "Classy"},
        {"word": "Friendly"},
        {"word": "Progressive"},
        {"word": "Sporty"},
        {"word": "Peaceful"},
        {"word": "Rich"},
        {"word": "Sweet"},
        {"word": "Hip"},
        {"word": "Great"},
        {"word": "Young"},
        {"word": "Strong"},
        {"word": "Faithful"},
        {"word": "Funny"},
        {"word": "Passionate"},
        {"word": "Fair"},
        {"word": "Cool"},
        {"word": "Unconstrained"},
        {"word": "Unaffected"},
        {"word": "Clever"},
        {"word": "Traveling"},
        {"word": "Global"},
        {"word": "Healthy"},
        {"word": "Witty"},
        {"word": "Be Loved"},
        {"word": "Calm"},
        {"word": "Famous"},
        {"word": "Interesting"},
        {"word": "Inspirational"},
        {"word": "Tough"},
        {"word": "Cute"},
        {"word": "Benevolent"},
        {"word": "Joyful"},
        {"word": "Well-known"},
        {"word": "Christian"},
        {"word": "Natural"},
        {"word": "Smart"},
        {"word": "Knowledgeable"},
        {"word": "Beatiful"},
        {"word": "Cheerful"},
        {"word": "Splendid"},
        {"word": "Unattached"},
        {"word": "Brave"},
        {"word": "Modest"},
        {"word": "Considerate"},
        {"word": "Respectful"},
        {"word": "Independent"},
        {"word": "Radical"},
        {"word": "Bold"},
        {"word": "Dignified"},
        {"word": "Brainy"},
        {"word": "Communicative"},
        {"word": "Open-minded"},
        {"word": "Free"},
        {"word": "Lots of hair"},
        {"word": "Strong Minded"},
        {"word": "Warm"},
        {"word": "Happy"},
        {"word": "Relaxed"},
        {"word": "Artistic"}

    ]
    db.wordEx.insert_many(wordEx)



insert()



