HttpService = game:GetService("HttpService")

function GetJson(v)
	return HttpService:JSONDecode(HttpService:GetAsync(v))
end

while true do
	pcall(function()
		Rand = GetJson("https://api.jihujiasuqi.com//apps/captcha/get.php").rand
		for i = 1, 360 do
			if GetJson("https://api.jihujiasuqi.com//apps/captcha/verify.php?rand="..Rand.."&angle="..i).okey then
				Random = ""
				for v = 0, 100 do
					Random = Random..string.char(math.random(97, 122))
				end
				print(GetJson("https://api.jihujiasuqi.com//api/user.php?mode=reg&mail="..Random.."@163.com&pwd="..Random.."&captcha_rand="..Rand).msg)
				break
			end
		end
	end)
end