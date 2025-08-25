# 'ab' - сокращение от 'a'ddress'b'ook
ab = { 'Swaroop' : 'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'
    }

print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение

del ab['Spammer']
print(ab)

print('В адресной книге {0} контакта'.format(len(ab)))