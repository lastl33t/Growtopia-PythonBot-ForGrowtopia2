from .hash import sha256, md5

def generate_klv(protocol: str, game_version: str, rid: str) -> str:
    salts = [
        "e9fc40ec08f9ea6393f59c65e37f750aacddf68490c4f92d0d2523a5bc02ea63",
        "c85df9056ee603b849a93e1ebab5dd5f66e1fb8b2f4a8caef8d13b9f9e013fa4",
        "3ca373dffbf463bb337e0fd768a2f395b8e417475438916506c721551f32038d",
        "73eff5914c61a20a71ada81a6fc7780700fb1c0285659b4899bc172a24c14fc1",
    ]

    part1 = sha256(md5(sha256(protocol)))
    part2 = salts[0]
    part3 = sha256(sha256(game_version))
    part4 = salts[1]
    part5 = sha256(md5(sha256(rid)))
    part6 = salts[2]
    part7 = sha256(sha256(protocol) + salts[3])

    combined = f"{part1}{part2}{part3}{part4}{part5}{part6}{part7}"
    return sha256(combined)