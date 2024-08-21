HttpService = game:GetService("HttpService")

function GetJson(v)
	return HttpService:JSONDecode(HttpService:GetAsync(v))
end

while true do
	pcall(function()
		local Rand = GetJson("https://api.jihujiasuqi.com/apps/captcha/get.php").rand
		for i = 30, 330, 30 do
			if GetJson("https://api.jihujiasuqi.com/apps/captcha/verify.php?rand="..Rand.."&angle="..i).okey then
				print(GetJson("https://api.jihujiasuqi.com/api/user.php?mode=reg&mail="..HttpService:GenerateGUID(false).."&captcha_rand="..Rand).msg)
				break
			end
		end
	end)
end
